import unittest
import copy
import random
import warnings

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


def tmp_reward(ans, **kwargs):
    bit_1, bit_2 = kwargs.get('input')
    correct = bit_1 ^ bit_2
    # print(f'Correct Ans: {correct}\t\tAns: {ans[0]}')
    return random.uniform(1, 2) * 10 if correct == ans[0] else -1 * random.uniform(1, 2) * 10


def solve_task(predict, **kwargs):
    return predict(kwargs.get('input'))
