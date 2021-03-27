from generation.Generation import Generation

class Evolution:

    def __init__(self, input_neurons, output_neurons, reward_function):
        self._input_neurons = input_neurons
        self._output_neurons = output_neurons
        self._reward = reward_function


    def start_simulation(self):
        generation = Generation()
        generation.start_simulation(first=True,
                                    input_neurons=self._input_neurons,
                                    output_neurons=self._output_neurons,
                                    reward_function=self._reward)


def tmp_reward(bit_1, bit_2, ans):
    correct = bit_1 ^ bit_2
    return 10 if correct == ans else -10


if __name__ == '__main__':
    evolution = Evolution(2, 2, tmp_reward)
    evolution.start_simulation()


