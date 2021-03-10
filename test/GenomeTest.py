import unittest

from genome.Genome import Genome

class GenomeTest(unittest.TestCase):

    def test_genome(self):
        genome_1 = Genome(generation_number=1, input_nodes=2, output_nodes=3)
        genome_2 = Genome(0, 3, 2)

