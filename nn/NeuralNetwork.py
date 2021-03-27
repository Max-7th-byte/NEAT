import copy

from nn.Neuron import Neuron
from util.NeuronType import NeuronType
from util.Status import Status


class NeuralNetwork:

    def __init__(self, genome=None):
        self._genome = genome
        self._score = 0

    def predict(self, _input):
        _input = copy.deepcopy(_input)
        # Validation of _input
        if not self._correct_input(_input):
            return -1

        # Append bias activation
        _input.append(1)

        # Initialize
        neurons = [Neuron(node) for node in self._genome.nodes()]
        for i in range(self._genome.input_nodes() + 1):
            neurons[i].set_activation(_input[i])

        # Calculate
        prediction = []
        for neuron in neurons:
            if neuron.node().type() == NeuronType.OUTPUT:
                activation = self._calculate_activation_recursively(neuron, neurons)
                neuron.set_activation(activation)
                prediction.append(1 if neuron.activation() > 0 else 0)

        return prediction


    def simulate(self, solve_task, **kwargs):
        return solve_task(self.predict, **kwargs)


    def mutate(self):
        self._genome.mutate()


    # TMP
    def add_node(self):
        self._genome._add_node()


    def add_connection(self):
        self._genome._add_connection()
    #####

    """ HELPERS """
    def _calculate_activation_recursively(self, neuron, neurons):
        activation = 0
        for con in neuron.node().connections_in():

            if con.status() != Status.ENABLED:
                continue

            # Looking for input neuron
            new_neuron = None
            for n in neurons:
                if n.node() == con.input_node():
                    new_neuron = n
                    break

            if new_neuron.activation() is not None:
                activation += new_neuron.activation() * con.weight()
            else:
                new_neuron_activation = self._calculate_activation_recursively(new_neuron, neurons) * con.weight()
                new_neuron.set_activation(new_neuron_activation)
                activation += new_neuron_activation * con.weight()

        return activation


    def _correct_input(self, _input):
        return len(_input) == self._genome.input_nodes()


    def genome(self):
        return self._genome

    def score(self):
        return self._score

    def set_score(self, score):
        self._score = score