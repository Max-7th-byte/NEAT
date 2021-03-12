from random import choice
from genome.ConnectGene import ConnectGene
from genome.NodeGene import NodeGene
from genome.util.NeuronType import NeuronType


class Genome:

    """
    Fields:

    connections -- a of connections between all neurons
    nodes -- list of neurons

    """

    def __init__(self, generation, input_nodes, output_nodes):
        self._connections = list()
        self._nodes = list()
        self._generation = generation
        self._output_nodes = output_nodes
        self._input_nodes = input_nodes

        self._init_nodes(input_nodes, output_nodes)
        self._init_connections(input_nodes)



    def mutate(self):
        pass


    def add_connection(self):
        connection, alreadyMutated = self._pick_connection()
        count = 0
        while (connection in self._connections) and (count < 50):
            connection, alreadyMutated = self._pick_connection()
            count += 1

        if count != 50:
            self._connections.append(connection)
            if not alreadyMutated:
                self._generation.increase()
        else:
            print('Connection was not added!')


    def _pick_nodes(self):

        in_node = choice(self._nodes[0:len(self._nodes) - self._output_nodes])
        out_node = choice(self._nodes[self._input_nodes + 1:])

        return in_node, out_node


    def _pick_connection(self):
        in_node, out_node = self._pick_nodes()
        connection = ConnectGene(in_node, out_node, -1)

        has_connection = True
        count = 0
        while has_connection and count < 50:
            if connection in self._connections:
                in_node, out_node = self._pick_nodes()
                connection = ConnectGene(in_node, out_node, -1)
            else:
                has_connection = False
            count += 1
        innov_number = self._generation.get_innovation_number(connection)
        connection.set_innovation_number(innov_number)
        return connection, has_connection


    def add_node(self):

        connection_to_split = choice(self._connections)

        node = NodeGene(NeuronType.HIDDEN, self._generation.node_id(), disabled_connection=connection_to_split)

        found = False
        for n in self._generation.nodes():
            if n.disabled_connection() is not None and \
                    n.disabled_connection().innovation_number() == \
                    node.disabled_connection().innovation_number():

                node.set_id(n.id())
                found = True
                break

        if not found:
            self._generation.increase_node_id()
            self._generation.nodes().append(node)

        connection_to_split.disable()

        innov_1 = self._generation.innovation_number()
        innov_2 = self._generation.innovation_number() + 1
        in_connection = ConnectGene(connection_to_split.input_node(), node, innov_1,
                                    weight_type="previous", weight=connection_to_split.weight())
        out_connection = ConnectGene(node, connection_to_split.output_node(), innov_2,
                                     weight_type="one")

        if found:
            pass
        else:
            self._generation.increase(2)

        node.set_con_in(in_connection)
        node.set_con_out(out_connection)

        self._nodes.append(node)
        self._connections.append(in_connection)
        self._connections.append(out_connection)


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

            input_node.set_con_out(new_connection)
            random_output_node.set_con_in(new_connection)
            self._generation.put_mutation(new_connection)
            self._connections.append(new_connection)

    def size(self):
        return len(self._connections) + len(self._nodes)

    def connections(self):
        return self._connections

    def nodes(self):
        return self._nodes
