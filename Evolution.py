from generation.Generation import Generation
from config import number_of_generations

class Evolution:

    def __init__(self, input_neurons, output_neurons, reward_function):
        self._input_neurons = input_neurons
        self._output_neurons = output_neurons
        self._reward = reward_function


    def start_simulation(self):
        generation = Generation()
        next_gen = generation.start_simulation(first=True,
                                               input_neurons=self._input_neurons,
                                               output_neurons=self._output_neurons,
                                               reward_function=self._reward)

        for i in range(number_of_generations - 1):
            next_gen = next_gen.start_simulation(self._reward,
                                                 input_neurons=self._input_neurons,
                                                 output_neurons=self._output_neurons)
