from random import uniform
import numpy as np
from genome.util.Status import Status

class ConnectGene:

    def __init__(self, input_node, output_node, innovation_number, weight_type="random", weight=0):

        self._input_node = input_node
        self._output_node = output_node
        if weight_type == "random":
            self._weight = uniform(-1, 1)
        elif weight_type == "one":
            self._weight = 1
        elif weight_type == "previous":
            self._weight = weight

        self._status = Status.ENABLED
        self._innovation_number = innovation_number


    def mutate(self):
        pass


    def __eq__(self, other):
        if self._input_node == other.input_node() and \
                self._output_node == other.output_node():
            return True

        return False


    def input_node(self):
        return self._input_node

    def output_node(self):
        return self._output_node

    def weight(self):
        return self._weight

    def disable(self):
        self._status = Status.DISABLED

    def innovation_number(self):
        return self._innovation_number

    def set_innovation_number(self, innov_number):
        self._innovation_number = innov_number

    def __str__(self):
        return f'[{self._input_node} --({np.around(self._weight, 2)})--> {self._output_node} ({self._innovation_number})]'
