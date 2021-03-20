import unittest

from generation.Generation import Generation
from genome.Genome import Genome
import visual.net as viz

class GenerationTest(unittest.TestCase):


    def test_evaluate(self):
        generation = Generation()
        generation.start_simulation(solve_task,
                                    tmp_reward,
                                    first=True,
                                    input_neurons=2,
                                    output_neurons=1,
                                    bit_1=1,
                                    bit_2=0)
        for i, org in enumerate(generation.organisms()):
            viz.construct(org, f'Organism {i}')


def tmp_reward(ans, **kwargs):
    correct = kwargs.get('bit_1') ^ kwargs.get('bit_2')
    print(f'Correct Ans: {correct}\t\tAns: {ans}')
    return 10 if correct == ans else -10


def solve_task(genome, **kwargs):
    return genome.predict(**kwargs)
