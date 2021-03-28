from config import sigma_threshold


class Species:

    def __init__(self, _id):
        self._id = _id
        self._representatives = list()


    def adjusted_fitness(self, fitness):
        pass


    def pick_parents(self):
        pass


    @staticmethod
    def sh(sigma):
        return 1 if sigma <= sigma_threshold else 0


    def representatives(self):
        return self._representatives

    def __str__(self):
        return f'Species ({self._id})'
