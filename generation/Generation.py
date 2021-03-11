

class Generation:


    def __init__(self):
        self._innovation_number = 1
        self._mutations = list()


    def get_innovation_number(self, connection):
        for mutation in self._mutations:
            if mutation == connection:
                return mutation.innovation_number()
        return self._innovation_number

    def innovation_number(self):
        return self._innovation_number

    def increase(self):
        self._innovation_number += 1

    def mutations(self):
        return self._mutations
