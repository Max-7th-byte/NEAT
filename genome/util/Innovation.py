
NUMBER = 0

class Innovation:

    def __init__(self, prev_connection, new_connection_1, new_connection_2):
        global NUMBER

        self._prev = prev_connection
        self._new_1 = new_connection_1
        self._new_2 = new_connection_2

        NUMBER += 1
        self._number = NUMBER


    def __eq__(self, other):
        return self._prev == other.prev and \
               self._new_1 == other.new_1 and \
               self._new_2 == other.new_2

    def number(self):
        return self._number


def reset():
    global NUMBER
    NUMBER = 0
