import unittest

from Species import Species


class SpeciesTest(unittest.TestCase):

    def test_max_ind(self):
        species = Species(1)
        for i in range(0, 15):
            species.append_fitness(i)

        for i in range(20, 10, -1):
            species.append_fitness(i)
        print(species.max_unchanged_for())
