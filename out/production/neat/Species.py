from config import sigma_threshold


class Species:


    def __init__(self, generation):
        self._generation = generation
        self._representatives = list()


    def adjusted_fitness(self, fitness):
        pass


    def pick_parents(self):
        pass


    @staticmethod
    def sh(sigma):
        return 1 if sigma <= sigma_threshold else 0
