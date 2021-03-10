from genome.util.NeuronType import NeuronType

class NodeGene:

    ID = 0

    def __init__(self, neuron_type: NeuronType):
        NodeGene.ID += 1
        self.id = NodeGene.ID
        self.status = neuron_type
