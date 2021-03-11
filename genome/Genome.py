from random import choice
from genome.ConnectGene import ConnectGene
from genome.NodeGene import NodeGene
from genome.util.NeuronType import NeuronType
from genome.util.Status import Status


# TODO: Replace -123 with innovation number
class Genome:

    """
    Fields:

    connections -- a of connections between all neurons
    nodes -- list of neurons

    """

    NODE_ID = 1

    def __init__(self, generation, input_nodes, output_nodes):
        self._connections = list()
        self._nodes = list()

        self.init_nodes(input_nodes, output_nodes)
        self.init_connections(input_nodes)

        self._generation = generation
        self._output_nodes = output_nodes
        self._input_nodes = input_nodes


    def mutate(self):
        pass


    def add_connection(self):
        connection = self.pick_connection()
        count = 0
        while (connection in self._connections) and (count < 50):
            connection = self.pick_connection()
            count += 1

        if count != 50:
            self._connections.append(connection)
        else:
            print('Connection was not added!')


    def pick_nodes(self):

        in_node = choice(self._nodes[0:len(self._nodes) - self._output_nodes])
        out_node = choice(self._nodes[self._input_nodes + 1:])

        while in_node == out_node:
            in_node = choice(self._nodes[0:len(self._nodes) - self._output_nodes])
            out_node = choice(self._nodes[self._input_nodes + 1:])

        return in_node, out_node


    def pick_connection(self):
        in_node, out_node = self.pick_nodes()
        return ConnectGene(in_node, out_node, -123)


    def add_node(self):

        node = NodeGene(NeuronType.HIDDEN, Genome.NODE_ID)
        Genome.NODE_ID += 1

        connection_to_split = choice(self._connections)

        connection_to_split.disable()
        in_connection = ConnectGene(connection_to_split.input_node(), node, -123, weight_type="prev",
                                    weight=connection_to_split.weight())
        out_connection = ConnectGene(node, connection_to_split.output_node(), -123, weight_type="one")

        self._nodes.append(node)
        self._connections.append(in_connection)
        self._connections.append(out_connection)


    def init_nodes(self, input_nodes, output_nodes):
        for node in range(input_nodes + 1):
            self._nodes.append(NodeGene(NeuronType.INPUT, Genome.NODE_ID))
            Genome.NODE_ID += 1
        for node in range(output_nodes):
            self._nodes.append(NodeGene(NeuronType.OUTPUT, Genome.NODE_ID))
            Genome.NODE_ID += 1

    def init_connections(self, input_nodes):
        for input_node in self._nodes[0:input_nodes + 1]:
            random_output_node = choice(self._nodes[input_nodes + 1:])
            self._connections.append(ConnectGene(input_node, random_output_node, -123))


    def size(self):
        return len(self._connections) + len(self._nodes)

    def connections(self):
        return self._connections

    def nodes(self):
        return self._nodes
