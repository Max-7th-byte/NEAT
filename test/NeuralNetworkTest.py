from genome.Genome import Genome
from nn.NeuralNetwork import NeuralNetwork
from generation.Generation import Generation
import unittest

from util.NeuronType import NeuronType
from visual.net import construct

class NeuralNetworkTest(unittest.TestCase):

    def test_predict(self):
        generation = Generation()
        genome = Genome(generation=generation, input_nodes=2, output_nodes=1)
        nn = NeuralNetwork(genome=genome)
        construct(nn.genome(), 'Before')
        nn.add_node()
        construct(nn.genome(), '1 Node Added')
        nn.add_node()
        construct(nn.genome(), '2 Nodes Added')
        nn.add_connection()
        construct(nn.genome(), 'Connection Added')
        print("CONNECTIONS")
        for con in nn.genome().connections():
            print(con)
        print("CONNECTIONS")


        for pred in nn.predict([13, 25]):
            print(pred)
