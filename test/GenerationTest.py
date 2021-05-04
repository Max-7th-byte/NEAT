import unittest
import random
import warnings

from Species import Species
from generation.Generation import Generation
import visual.net as viz

class GenerationTest(unittest.TestCase):


    def test_evaluate(self):
        generation = Generation()

        generation.step(solve_task,
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
        generation.step(solve_task, tmp_reward, first=True, input_neurons=2, output_neurons=1, input=[0, 1])
        for i, org in enumerate(generation.organisms()):
            # viz.construct(org.genome(), f'Organism {i}')
            print(f'Organism {i}:', org.species())

        for species in generation.species():
            print(species)
            for i, rep in enumerate(species.representatives()):
                print(f'Representative {i}: {rep}')

    def test_eliminate(self):
        generation = Generation()
        generation.spawn(input_neurons=2, output_neurons=1)
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

    def test_reproduce(self):

        generation = Generation()
        new_gen = generation.step(input_neurons=3,
                                  output_neurons=2,
                                  reward_function=tmp_reward,
                                  solve_task=solve_task,
                                  _input=[0, 1, 0])
        print(new_gen.id())


def tmp_reward(ans, **kwargs):
    correct = [kwargs['_input'][0] ^ kwargs['_input'][1], kwargs['_input'][1] ^ kwargs['_input'][2]]
    return random.uniform(1, 2) * 10 if correct == ans else random.uniform(1, 2)


def solve_task(predict, **kwargs):
    return predict(kwargs['_input'])
