from config import population_size
from genome.Genome import Genome

class Generation:


    def __init__(self, data=None):
        self._innovation_number = 1
        self._node_id = 1
        self._initialized_first_genome = False

        if data is not None:
            self._organisms = data[0]
            self._mutations = data[1]
            self._nodes = data[2]
        else:
            self._mutations = list()
            self._nodes = list()
            self._organisms = list()



    def spawn(self, first=True, input_neurons=0, output_neurons=1):
        if first:
            for i in range(population_size):
                # Spawn new Genome with number of input/output neurons
                genome = Genome(self, input_neurons, output_neurons)
                self.add_organism(genome)
        else:
            pass


    def evaluate(self, reward_function):
        pass


    def speciation(self):
        pass


    def eliminate(self):
        pass


    def mutate(self):
        pass


    def crossover(self):
        pass


    def start_simulation(self, reward_function, first=False, input_neurons=0, output_neurons=1):
        self.spawn(first=first, input_neurons=input_neurons, output_neurons=output_neurons)
        self.evaluate(reward_function)
        self.speciation()
        self.eliminate()
        self.mutate()
        self.crossover()

        return Generation(data=(self._organisms, self._mutations, self._nodes))

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
