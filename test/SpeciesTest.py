import unittest

from Species import Species


class SpeciesTest(unittest.TestCase):

    def test_max_ind(self):
        species = Species(1)
        for i in range(17, 0, -1):
            species.append_fitness(i)

        print(species.max_unchanged_for())
