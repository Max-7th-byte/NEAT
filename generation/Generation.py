

class Generation:


    def __init__(self):
        self._innovation_number = 1
        self._node_id = 1
        self._mutations = list()
        self._nodes = list()
        self._organisms = list()
        self._initialized_first_genome = False



    def spawn(self, first=True):
        pass


    def evaluate(self):
        pass


    def speciation(self):
        pass


    def eliminate(self):
        pass


    def mutate(self):
        pass


    def crossover(self):
        pass


    def start_simulation(self):
        pass


    def get_innovation_number(self, connection):
        for mutation in self._mutations:
            if mutation == connection:
                return mutation.innovation_number()

        self.increase()
        return self._innovation_number - 1


    def innovation_number(self):
        return self._innovation_number

    def node_id(self):
        return self._node_id

    def increase_node_id(self):
        self._node_id += 1

    def increase(self, times=1):
        self._innovation_number += times

    def mutations(self):
        return self._mutations


    def put_mutation(self, mutation):
        found = False
        for mut in self._mutations:
            if mutation == mut:
                found = True
                break
        if not found:
            self._mutations.append(mutation)


    def nodes(self):
        return self._nodes

    def has_first_genome(self):
        return self._initialized_first_genome

    def put_first_genome(self):
        self._initialized_first_genome = True

    def add_organism(self, organism):
        self._organisms.append(organism)

    def organisms(self):
        return self._organisms
