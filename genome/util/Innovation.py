
_NUMBER = 0

class Innovation:

    def __init__(self, _type="Node", new_node=None, new_connection=None):
        global _NUMBER

        self.new_node = new_node
        self.type = _type
        self.new_connection = new_connection

        _NUMBER += 1
        self._number = _NUMBER


    def __eq__(self, other):
        if self.type == "Node":
            return self.new_node == other.new_node
        else:
            return self.new_connection == other.new_connection


    def number(self):
        return self._number


def reset():
    global _NUMBER
    _NUMBER = 0
