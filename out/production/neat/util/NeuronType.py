from enum import Enum

class NeuronType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3


    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
