
class Neuron:

    def __init__(self, node):
        self._node = node
        self._activation = None

    def __str__(self):
        return str(self._node) + f' ({self._activation});'

    def set_activation(self, activation):
        self._activation = activation

    def update_activation(self, activation):
        if self._activation is None:
            self.set_activation(activation)
        else:
            self._activation += activation

    def node(self):
        return self._node

    def activation(self):
        return self._activation
