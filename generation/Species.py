
class Species:

    def __init__(self, _id):
        self._id = _id
        self._representatives = list()


    def adjusted_fitness(self):
        sum_adjusted_fitness = 0
        for org in self._representatives:
            sum_adjusted_fitness += org.score()
        return sum_adjusted_fitness/len(self._representatives)


    def representatives(self):
        return self._representatives

    def __str__(self):
        return f'Species ({self._id})'
