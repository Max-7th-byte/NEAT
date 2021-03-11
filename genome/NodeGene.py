from genome.util.NeuronType import NeuronType

class NodeGene:

    def __init__(self, neuron_type: NeuronType, id):
        self._type = neuron_type
        self._id = id


    def __eq__(self, other):
        return self._id == other.id()


    def id(self):
        return self._id


    def type(self):
        return self._type


    def __str__(self):
        return f'({self._id}, {self._type})'
