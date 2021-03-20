from enum import Enum

class Status(Enum):
    DISABLED = 0
    ENABLED = 1

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
