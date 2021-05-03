from generation.Generation import Generation
# TMP
import random
#

class Evolution:

    def __init__(self, input_neurons, output_neurons, reward_function):
        self._input_neurons = input_neurons
        self._output_neurons = output_neurons
        self._reward = reward_function


    def start_simulation(self):

        # TODO: change True to some other function
        prev_generation = None

        generation = Generation()
        generation.start_simulation(input_neurons=self._input_neurons,
                                    output_neurons=self._output_neurons,
                                    reward_function=self._reward,
                                    solve_task=solve_task,
                                    _input=[0, 1])


def tmp_reward(ans, **kwargs):
    correct = kwargs['_input'][0] ^ kwargs['_input'][1]
    print(f'ans: {ans}')
    return random.uniform(1, 2) * 10 if correct == ans[0] else random.uniform(1, 2) * -10


def solve_task(predict, **kwargs):
    return predict(kwargs['_input'])


if __name__ == '__main__':
    evolution = Evolution(2, 1, tmp_reward)
    evolution.start_simulation()
