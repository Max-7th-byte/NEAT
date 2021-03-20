import unittest
import copy

from genome.Genome import Genome
from generation.Generation import Generation
import visual.net as viz

class GenomeTest(unittest.TestCase):


    def test_init_1(self):
        print("\n\ntest_init_1.1")
        generation = Generation()
        genome = Genome(generation=generation, input_nodes=2, output_nodes=2)
        for con in genome.connections():
            print(con)

        for node in genome.nodes():
            print(node)

        print('-' * 40)

        for node in generation.nodes():
            print(node)

        print('-' * 60)
        viz.construct(genome, 'first')
        print("\n\ntest_init_1.2")
        genome_1 = Genome(generation, 2, 2)
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)

        print('-' * 40)

        for node in generation.nodes():
            print(node)
        viz.construct(genome_1, 'second')

        print('-' * 20 + 'Mutations')
        for mutation in generation.mutations():
            print(mutation)


    def test_init_2(self):

        generation = Generation()
        genome = Genome(generation=generation, input_nodes=1, output_nodes=1)
        genome._add_node()

        new_generation = Generation(_copy=True, generation=generation)
        genome_copied = Genome(generation=new_generation, _copy=True, genome_to_copy=genome)

        for node in generation.nodes():
            print(node)
        print('-' * 20)

        viz.construct(genome, 'first_1')
        genome_copied._add_node()

        for node in new_generation.nodes():
            print(node)
        viz.construct(genome_copied, 'first_copied_1')


    def test_add_connection(self):
        print('\n\ntest_add_connection\nBEFORE 0')
        generation = Generation()
        genome = Genome(generation, 1, 2)
        for con in genome.connections():
            print(con)
        viz.construct(genome, 'before_0')
        genome._add_connection()
        print('\nAFTER 0\n')
        for con in genome.connections():
            print(con)
        viz.construct(genome, 'after_0')

        genome_1 = Genome(generation, 1, 2)
        print('\n\ntest_add_connection\nBEFORE 1')
        for con in genome_1.connections():
            print(con)
        viz.construct(genome_1, 'before_1')
        genome_1._add_connection()
        print('\nAFTER 1\n')
        for con in genome_1.connections():
            print(con)
        viz.construct(genome_1, 'after_1')


    def test_add_node(self):

        print('-' * 20 + 'test_add_node\nBEFORE 0')
        generation = Generation()
        genome = Genome(generation, 1, 1)

        for con in genome.connections():
            print(con)

        for node in genome.nodes():
            print(node)

        viz.construct(genome, 'before_0')

        genome._add_node()
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

        genome_1 = Genome(generation, 1, 1)
        viz.construct(genome_1, 'before_1')
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)

        genome_1._add_node()

        print('\nAFTER 0 \n')
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)
        viz.construct(genome_1, 'after_1')
