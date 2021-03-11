import unittest

from genome.Genome import Genome
import visual.net as viz

class GenomeTest(unittest.TestCase):

    def test_genome(self):
        genome_1 = Genome(0, 2, 1)
        genome_2 = Genome(0, 2, 1)
        # viz.construct(genome_1)
        genome_1.add_connection()
        viz.construct(genome_1)
