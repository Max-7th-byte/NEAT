import numpy as np

from config import max_no_of_generations_fitness_not_growing as max_size

class Species:

    def __init__(self, _id):
        self._id = _id
        self._representatives = list()
        self._fitnesses = list()
        self._max_remain_unchanged = 0


    def adjusted_fitness(self):
        sum_adjusted_fitness = 0
        for org in self._representatives:
            sum_adjusted_fitness += org.score()
        return sum_adjusted_fitness/len(self._representatives)


    def representatives(self):
        return self._representatives

    def size(self):
        return len(self._representatives)

    def append_fitness(self, fitness):
        if len(self._fitnesses) == max_size + 1:
            del self._fitnesses[0]
        self._fitnesses.append(fitness)


    def max_unchanged_for(self):
        if len(self._fitnesses) == 0:
            return 0
        return max_size - np.argmax(np.array(self._fitnesses))


    def get_new_size(self, species_ad_fitness):
        return (self.adjusted_fitness()/species_ad_fitness) * len(self._representatives)


    # TODO: implement
    def get_champion(self):
        pass

    def is_champion(self, org):
        pass
    #

    def empty_species(self):
        return Species(self._id)


    def __eq__(self, other):
        if other is None:
            return False
        return self._id == other.id()


    def __hash__(self):
        return hash(self._id)


    def id(self):
        return self._id


    def __str__(self):
        return f'Species ({self._id})'
