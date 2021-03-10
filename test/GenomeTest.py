import unittest

from genome.Genome import Genome
import visual.net as viz

class GenomeTest(unittest.TestCase):

    def test_genome(self):
        genome_1 = Genome(generation_number=0, input_nodes=2, output_nodes=3)
        genome_2 = Genome(0, 3, 2)
        viz.construct(genome_2)
