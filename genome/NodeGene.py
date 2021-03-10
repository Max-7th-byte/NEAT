from genome.util.NeuronType import NeuronType

class NodeGene:

    ID = 0

    def __init__(self, neuron_type: NeuronType, innovation_number):
        NodeGene.ID += 1
        self._id = NodeGene.ID
        self._status = neuron_type
        self._innovation_number = innovation_number


    def __eq__(self, other):
        return self._id == other.id() and \
               self._innovation_number == other.innovation_number()


    def id(self):
        return self._id

    def innovation_number(self):
        return self._innovation_number

    def __str__(self):
        return f'Node({self._id}, {self._status})'

    @staticmethod
    def reset():
        NodeGene.ID = 0
