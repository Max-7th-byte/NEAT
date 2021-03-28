import unittest
import copy

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
        generation.start_simulation(solve_task, tmp_reward, first=True, input_neurons=2, output_neurons=1)
        for i, org in enumerate(generation.organisms()):
            viz.construct(org.genome(), f'Organism {i}')
            print(f'Organism {i}:', org.species())


def tmp_reward(ans, **kwargs):
    bit_1, bit_2 = kwargs.get('input')
    correct = bit_1 ^ bit_2
    print(f'Correct Ans: {correct}\t\tAns: {ans[0]}')
    return 10 if correct == ans[0] else -10


def solve_task(predict, **kwargs):
    return predict(kwargs.get('input'))
