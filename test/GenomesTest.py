import unittest

from generation.util.Genomes import _excesses_disjoints, produce_offspring, sigma
from genome.Genome import Genome
from generation.Generation import Generation
import visual.net as viz

class GenomeTest(unittest.TestCase):


    def test_offspring(self):

        generation = Generation()
        genome_1 = Genome(generation, 2, 2)
        genome_2 = Genome(generation, 2, 2)
        # for i in range(2):
        #     genome_1._add_connection()
        #     genome_2._add_connection()
        # for i in range(1):
        #     genome_1._add_node()
        #     genome_2._add_node()

        viz.construct(genome_1, 'Genome 1')
        viz.construct(genome_2, 'Genome 2')

        for con in genome_1.connections():
            print(con)
        print('-' * 40)
        for con in genome_2.connections():
            print(con)

        genome = produce_offspring(generation, genome_1, genome_2)
        print('-' * 40)
        for node in genome.nodes():
            print(node)

        print('\n' + '-' * 40)

        for con in genome.connections():
            print(con)

        viz.construct(genome, 'offspring')

        E, D = _excesses_disjoints(genome_1, genome_2)
        print('-' * 20)
        print(f'Excesses: {E}')
        print(f'Disjoints: {D}')


    def test_excesses_and_disjoints(self):

        generation = Generation()
        genome_1 = Genome(generation, 1, 2)
        genome_2 = genome_1.copy_genome()
        viz.construct(genome_1, 'First Before')
        genome_1._add_node()
        genome_1._add_connection()
        for con in genome_1.connections():
            print(con)
        viz.construct(genome_1, 'First')
        genome_2._add_node()
        viz.construct(genome_2, 'Second')
        E, D = _excesses_disjoints(genome_1, genome_2)
        print('-' * 20)
        for con in genome_2.connections():
            print(con)
        print(f'Excesses: {E}')
        print(f'Disjoints: {D}')


    def test_sigma(self):

        generation = Generation()

        genome_1 = Genome(generation, 1, 1)
        genome_2 = genome_1.copy_genome()

        # genome_1._add_node()
        genome_1._mutate_weights()
        genome_2._mutate_weights()

        for con in genome_1.connections():
            print(con)

        print('-' * 20)
        for con in genome_2.connections():
            print(con)
        print(sigma(genome_1, genome_2))
