

class Generation:


    def __init__(self):
        self._innovation_number = 1
        self._mutations = list()


    def innovation_number(self):
        return self._innovation_number

    def increase(self):
        self._innovation_number += 1
