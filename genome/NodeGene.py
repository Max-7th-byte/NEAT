from genome.util.NeuronType import NeuronType

class NodeGene:

    def __init__(self, neuron_type: NeuronType, _id, con_in=None, con_out=None, disabled_connection=None):
        self._type = neuron_type
        self._id = _id
        self._connections_in = []
        self._connections_out = []
        if con_in is not None:
            self._connections_in.append(con_in)

        if con_out is not None:
            self._connections_out.append(con_out)
        self._disabled_connection = disabled_connection


    def __eq__(self, other):
        return self._id == other.id()


    def copy_without_connections(self):
        return NodeGene(self._type, self._id, con_in=None, con_out=None, disabled_connection=self._disabled_connection)


    def copy_node(self):
        pass


    def append_con_in(self, con_in):
        self._connections_in.append(con_in)

    def append_con_out(self, con_out):
        self._connections_out.append(con_out)

    def id(self):
        return self._id

    def type(self):
        return self._type

    def connections_in(self):
        return self._connections_in

    def connections_out(self):
        return self._connections_out

    def disabled_connection(self):
        return self._disabled_connection

    def set_id(self, _id):
        self._id = _id

    def __str__(self):
        return f'({self._id}, {self._type}; ' \
            f'input_cons: {["(" + str(con.innovation_number()) + ")" for con in self._connections_in]}; ' \
            f'output_cons: {["(" + str(con.innovation_number()) + ")" for con in self._connections_out]})'
