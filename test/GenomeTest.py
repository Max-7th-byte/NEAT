import unittest

from genome.Genome import Genome
from generation.Generation import Generation
import visual.net as viz

class GenomeTest(unittest.TestCase):

    def test_genome(self):
        pass



    # def test_init(self):
    #     print("\n\ntest_init")
    #     generation = Generation()
    #     genome = Genome(generation, 2, 1)
    #     for con in genome.connections():
    #         print(con)
    #
    #     for node in genome.nodes():
    #         print(node)


    def test_add_connection(self):
        print('\n\ntest_add_connection\nBEFORE')
        generation = Generation()
        genome = Genome(generation, 1, 2)
        for con in genome.connections():
            print(con)

        print(generation.innovation_number())
        genome.add_connection()
        print('\nAFTER\n')
        for con in genome.connections():
            print(con)
        print(generation.innovation_number())


