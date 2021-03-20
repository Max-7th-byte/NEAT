from random import uniform
import numpy as np
from genome.util.Status import Status

class ConnectGene:

    def __init__(self, input_node, output_node, innovation_number, weight_type="random", weight=0):

        self._input_node = input_node
        self._output_node = output_node
        if weight_type == "random":
            self._weight = float(np.around(uniform(-1, 1), 2))
        elif weight_type == "one":
            self._weight = 1
        elif weight_type == "previous":
            self._weight = weight

        self._status = Status.ENABLED
        self._innovation_number = innovation_number


    def mutate(self):
        pass


    def __eq__(self, other):
        if other is None:
            return False
        return self._input_node == other.input_node() and \
               self._output_node == other.output_node()



    def __hash__(self):
        return hash((self._input_node, self._output_node))


    def input_node(self):
        return self._input_node

    def output_node(self):
        return self._output_node

    def weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def uniformly_perturbed(self, value):
        self._weight += value

    def disable(self):
        self._status = Status.DISABLED

    def enable(self):
        self._status = Status.ENABLED

    def innovation_number(self):
        return self._innovation_number

    def set_innovation_number(self, innov_number):
        self._innovation_number = innov_number

    def status(self):
        return self._status

    def __str__(self):
        return f'[{self._input_node}] ---({self._status})({self._weight})---> [{self._output_node} ({self._innovation_number})]'
