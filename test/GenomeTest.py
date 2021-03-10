import unittest

from genome.Genome import Genome

class GenomeTest(unittest.TestCase):

    def test_genome(self):
        genome_1 = Genome(0, 3, 2)
        genome_2 = Genome(0, 3, 2)
        for con in genome_1.connections():
            print(con)

        for node in genome_1.nodes():
            print(node)
