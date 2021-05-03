import unittest
import random
import warnings

from Species import Species
from generation.Generation import Generation
import visual.net as viz

class GenerationTest(unittest.TestCase):


    def test_evaluate(self):
        generation = Generation()

        generation.start_simulation(solve_task,
                                    tmp_reward,
                                    first=True,
                                    input_neurons=2,
                                    output_neurons=1,
                                    input=[0, 1])
        for i, org in enumerate(generation.organisms()):
            viz.construct(org.genome(), f'Organism {i}')
            print(org.score())


    def test_speciation(self):
        generation = Generation()
        generation.start_simulation(solve_task, tmp_reward, first=True, input_neurons=2, output_neurons=1, input=[0, 1])
        for i, org in enumerate(generation.organisms()):
            # viz.construct(org.genome(), f'Organism {i}')
            print(f'Organism {i}:', org.species())

        for species in generation.species():
            print(species)
            for i, rep in enumerate(species.representatives()):
                print(f'Representative {i}: {rep}')

    def test_eliminate(self):
        generation = Generation()
        generation.spawn(first=True, input_neurons=2, output_neurons=1)
        for org in generation.organisms():
            org.add_node()
            org.add_node()
            org.add_connection()
        generation.evaluate(solve_task, tmp_reward, input=[0, 1])
        generation.speciation()
        print('\n\nBefore elimination')
        print('Organisms')
        for i, org in enumerate(generation.organisms()):
            print(i, org)
        print('Species')
        for species in generation.species():
            print(species)
            for rep in species.representatives():
                print(rep)
        generation.eliminate()
        print('\n\nAFTER ELIMINATION')
        for i, org in enumerate(generation.organisms()):
            print(i, org)
        print('Species')
        for species in generation.species():
            print(species)
            for rep in species.representatives():
                print(rep)
        for i, org in enumerate(generation.organisms()):
            # viz.construct(org.genome(), f'Organism {i}')
            print(f'Organism {i}:', org.species())

        for species in generation.species():
            print(species)
            for i, rep in enumerate(species.representatives()):
                print(f'Representative {i}: {rep}')

    def test_mutate(self):
        generation = Generation()
        generation.spawn(first=True, input_neurons=2, output_neurons=1)
        generation.speciation()

        print('BEFORE MUTATE')
        for i, org in enumerate(generation.organisms()):
            print(f'Genome {i}')
            for con in org.genome().connections():
                print(con)
            warnings.simplefilter('ignore', ResourceWarning)
            viz.construct(org.genome(), f'Organism {i}')

        generation.mutate()

        print('AFTER MUTATE')
        for i, org in enumerate(generation.organisms()):
            print(f'Genome {10 + i}')
            for con in org.genome().connections():
                print(con)
            warnings.simplefilter('ignore', ResourceWarning)
            viz.construct(org.genome(), f'Organism {10 + i}')

    def test_reproduce(self):

        generation = Generation()
        species = Species(4)
        for i in range(20, 0, -1):
            species.append_fitness(i)

        generation.species().append(species)
        for i in range(4):
            species = Species(i * 3)
            for j in range(20):
                species.append_fitness(j)
            generation.species().append(species)
        generation.reproduce()

        for species in generation.species():
            print(species)

def tmp_reward(ans, **kwargs):
    bit_1, bit_2 = kwargs.get('input')
    correct = bit_1 ^ bit_2
    return random.uniform(1, 2) * 10 if correct == ans[0] else -1 * random.uniform(1, 2) * 10


def solve_task(predict, **kwargs):
    return predict(kwargs.get('input'))
