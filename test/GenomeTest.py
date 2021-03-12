import unittest
import copy

from genome.Genome import Genome
from generation.Generation import Generation
import visual.net as viz

class GenomeTest(unittest.TestCase):


    # def test_init(self):
    #     print("\n\ntest_init")
    #     generation = Generation()
    #     genome = Genome(generation, 2, 2)
    #     for con in genome.connections():
    #         print(con)
    #
    #     for node in genome.nodes():
    #         print(node)
    #
    #     print('-' * 40)
    #
    #     for node in generation.nodes():
    #         print(node)
    #
    #     print('-' * 60)
    #     viz.construct(genome, 'first')
    #     print("\n\ntest_init_1")
    #     genome_1 = Genome(generation, 2, 2)
    #     for con in genome_1.connections():
    #         print(con)
    #
    #     for node in genome_1.nodes():
    #         print(node)
    #
    #     print('-' * 40)
    #
    #     for node in generation.nodes():
    #         print(node)
    #     viz.construct(genome_1, 'second')
    #
    #     print('-' * 20 + 'Mutations')
    #     for mutation in generation.mutations():
    #         print(mutation)

    # def test_add_connection(self):
    #     print('\n\ntest_add_connection\nBEFORE')
    #     generation = Generation()
    #     genome = Genome(generation, 1, 2)
    #     for con in genome.connections():
    #         print(con)
    #     viz.construct(genome, 'before')
    #     genome.add_connection()
    #     print('\nAFTER\n')
    #     for con in genome.connections():
    #         print(con)
    #     viz.construct(genome, 'after')


    def test_add_node(self):

        print('-' * 20 + 'test_add_node\nBEFORE 0')
        generation = Generation()
        genome = Genome(generation, 2, 2)

        for con in genome.connections():
            print(con)

        for node in genome.nodes():
            print(node)

        viz.construct(genome, 'before_0')

        genome.add_node()
        for node in generation.nodes():
            print(node)
        print('\nAFTER 0 \n')
        for con in genome.connections():
            print(con)

        print('-' * 40)
        for node in genome.nodes():
            print(node)
        viz.construct(genome, 'after_0')

        print('\n\ntest_add_node\nBEFORE 1')

        genome_1 = Genome(generation, 2, 2)
        viz.construct(genome_1, 'before_1')
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)

        genome_1.add_node()

        print('\nAFTER 0 \n')
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)
        viz.construct(genome_1, 'after_1')
