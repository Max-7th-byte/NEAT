from Genome import Genome

class NeuralNetwork():

    def __init__(self, generation=None, input_nodes=1, output_nodes=1, connections=True, _copy=False, genome_to_copy=None):
        self._genome = Genome(generation, input_nodes, output_nodes, connections, _copy, genome_to_copy)
