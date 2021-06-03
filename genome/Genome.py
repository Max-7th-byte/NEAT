from random import choice
import random
import copy

from genome.ConnectGene import ConnectGene
from genome.NodeGene import NodeGene
from genome.util.NeuronType import NeuronType

from config import weights_mutation, weight_uniformly_perturbed, \
     random_weight, new_link_rate, new_link_rate_large_species, min_no_for_large_species, \
     new_node_rate, gauss_mu, gauss_sigma
from util.Status import Status

class Genome:

    def __init__(self, generation=None, input_nodes=1, output_nodes=1, connections=True, _copy=False, genome_to_copy=None):
        if not _copy:
            # Creating completely new Genome
            self._connections = list()
            self._nodes = list()
            self._generation = generation
            self._output_nodes = output_nodes
            self._input_nodes = input_nodes

            self._init_nodes(input_nodes, output_nodes)
            # TODO: do not init connections
            if connections:
                self._init_connections(input_nodes)

        elif genome_to_copy is not None:
            # Copying very successful Genome
            self._connections = copy.deepcopy(genome_to_copy.connections())
            self._nodes = copy.deepcopy(genome_to_copy.nodes())
            self._generation = genome_to_copy.generation()
            self._input_nodes = genome_to_copy.input_nodes()
            self._output_nodes = genome_to_copy.output_nodes()
        else:
            raise ValueError('Wrong arguments were passed')

    def mutate(self, species_size):
        self._mutate_weights()
        self._mutate_node()
        self._mutate_connection(species_size)

    def _mutate_weights(self):
        for con in self._connections:
            if con.is_enabled():
                chance = random.uniform(0, 1)
                if chance < weights_mutation:
                    chance = random.uniform(0, 1)
                    if chance < weight_uniformly_perturbed:
                        value = random.gauss(gauss_mu, gauss_sigma)
                        con.uniformly_perturbed(value)

                    chance = random.uniform(0, 1)
                    if chance < random_weight:
                        value = random.uniform(0, 1)
                        con.set_weight(value)


    def _mutate_node(self):
        chance = random.uniform(0, 1)
        if chance < new_node_rate:
            self._add_node()


    def _mutate_connection(self, species_size):
        chance = random.uniform(0, 1)
        if species_size <= min_no_for_large_species:
            if chance < new_link_rate:
                self._add_connection()
        else:
            if chance < new_link_rate_large_species:
                self._add_connection()


    """
    Defines how a connection can be added as a result of mutation 
    """
    def _add_connection(self):
        connection, already_here = self._pick_connection()

        if not already_here:
            self._connections.append(connection)
            self._generation.put_mutation(connection)



    def _pick_nodes(self):

        without_output = []
        for node in self._nodes:
            if node.type() is not NeuronType.OUTPUT:
                without_output.append(node)

        in_node = choice(without_output)
        out_node = choice(self._nodes[self._input_nodes + 1:])
        while out_node == in_node or ConnectGene(out_node, in_node, 0) in self._connections:
            out_node = choice(self._nodes[self._input_nodes + 1:])

        return in_node, out_node


    def _pick_connection(self):
        from_node, to_node = self._pick_nodes()
        connection = ConnectGene(from_node, to_node, -1)

        has_connection = True
        count = 0
        while has_connection and count < 10:
            if connection in self._connections:
                from_node, to_node = self._pick_nodes()
                connection = ConnectGene(from_node, to_node, -1)
            else:
                has_connection = False
                from_node.append_con_out(connection)
                to_node.append_con_in(connection)
            count += 1
        innov_number = self._generation.get_innovation_number(connection)
        connection.set_innovation_number(innov_number)
        return connection, has_connection


    def _add_node(self):
        connection_to_split = self._choose_connection()
        node = NodeGene(NeuronType.HIDDEN, self._generation.node_id(), disabled_connection=connection_to_split)

        found = self._set_node_id(node)

        connection_to_split.disable()

        in_connection, out_connection = self._create_new_connections(found, node, connection_to_split)

        node.append_con_in(in_connection)
        node.append_con_out(out_connection)
        connection_to_split.input_node().append_con_out(in_connection)
        connection_to_split.output_node().append_con_in(out_connection)

        self._connections.append(in_connection)
        self._connections.append(out_connection)

        self._nodes.append(node)

    def _choose_connection(self):
        con_to_split = choice(self._connections)
        while con_to_split.status() != Status.ENABLED:
            con_to_split = choice(self._connections)
        return con_to_split

    def _set_node_id(self, node):
        for n in self._generation.nodes():
            if n.disabled_connection() is not None and \
                    n.disabled_connection().innovation_number() == \
                    node.disabled_connection().innovation_number():
                node.set_id(n.id())
                return True

        self._generation.increase_node_id()
        self._generation.nodes().append(node)
        return False


    def _create_new_connections(self, found, node, connection_to_split):
        innov_1 = self._generation.innovation_number()
        innov_2 = self._generation.innovation_number() + 1
        in_connection = ConnectGene(connection_to_split.input_node(), node, innov_1,
                                    weight_type="previous", weight=connection_to_split.weight())
        out_connection = ConnectGene(node, connection_to_split.output_node(), innov_2,
                                     weight_type="one")

        both = 0
        if found:
            for mut in self._generation.mutations():

                if mut == in_connection:
                    in_connection.set_innovation_number(mut.innovation_number())
                    both += 1
                if mut == out_connection:
                    out_connection.set_innovation_number(mut.innovation_number())
                    both += 1

                if both == 2:
                    break
        else:
            self._generation.increase(2)
            self._generation.mutations().append(in_connection)
            self._generation.mutations().append(out_connection)

        return in_connection, out_connection

    def _init_nodes(self, input_nodes, output_nodes):
        if self._generation.has_first_genome():
            self._init_nodes_has_first(input_nodes, output_nodes)
        else:
            self._init_node_not_first(input_nodes, output_nodes)


    def _init_nodes_has_first(self, input_nodes, output_nodes):
        _id = 1
        for n in range(input_nodes + 1):
            node = NodeGene(NeuronType.INPUT, _id)
            self._nodes.append(node)
            _id += 1

        for n in range(output_nodes):
            node = NodeGene(NeuronType.OUTPUT, _id)
            self._nodes.append(node)
            _id += 1


    def _init_node_not_first(self, input_nodes, output_nodes):
        for n in range(input_nodes + 1):
            node = NodeGene(NeuronType.INPUT, self._generation.node_id())
            self._nodes.append(node)
            self._generation.nodes().append(node)
            self._generation.increase_node_id()

        for n in range(output_nodes):
            node = NodeGene(NeuronType.OUTPUT, self._generation.node_id())
            self._nodes.append(node)
            self._generation.nodes().append(node)
            self._generation.increase_node_id()

        self._generation.put_first_genome()


    def _init_connections(self, input_nodes):
        for input_node in self._nodes[0:input_nodes + 1]:
            random_output_node = choice(self._nodes[input_nodes + 1:])
            new_connection = ConnectGene(input_node, random_output_node, -1)
            new_connection.set_innovation_number(self._generation.get_innovation_number(new_connection))

            input_node.append_con_out(new_connection)
            random_output_node.append_con_in(new_connection)
            self._generation.put_mutation(new_connection)
            self._connections.append(new_connection)


    def copy_genome(self):
        copied = Genome(self._generation, self._input_nodes, self._output_nodes, connections=False)
        copied._connections = copy.deepcopy(self._connections)
        copied._nodes = copy.deepcopy(self._nodes)
        return copied

    def size(self):
        return len(self._connections)

    def connections(self):
        return self._connections

    def nodes(self):
        return self._nodes

    def append_to_nodes(self, node):
        self._nodes.append(node)

    def input_nodes(self):
        return self._input_nodes

    def output_nodes(self):
        return self._output_nodes

    def generation(self):
        return self._generation

    def set_generation(self, new_gen):
        self._generation = new_gen
