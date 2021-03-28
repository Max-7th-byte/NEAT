import copy

from config import population_size, sigma_threshold
from genome.Genome import Genome
from nn.NeuralNetwork import NeuralNetwork
from generation.Species import Species
import generation.util.Genomes as gens


class Generation:


    def __init__(self, _copy=False, generation=None):
        self._initialized_first_genome = False

        if not _copy:
            self._innovation_number = 1
            self._node_id = 1
            self._species_number = 1
            self._mutations = list()
            self._nodes = list()
            self._organisms = list()
            self._species = list()
        else:
            self._organisms = copy.deepcopy(generation.organisms())
            self._mutations = copy.deepcopy(generation.mutations())
            self._nodes = copy.deepcopy(generation.nodes())
            self._innovation_number = generation.innovation_number()
            self._node_id = generation.node_id()
            self._species_number = generation.species_number()
            self._species = generation.species()



    def spawn(self, first=True, input_neurons=0, output_neurons=1):
        if first:
            for i in range(population_size):
                # Spawn new Genome with number of input/output neurons
                genome = Genome(self, input_neurons, output_neurons)
                nn = NeuralNetwork(genome)
                self.add_organism(nn)
        else:
            pass


    def evaluate(self, solve_task, reward_function, **kwargs):
        for org in self._organisms:
            result = org.simulate(solve_task, **kwargs)
            org.set_score(reward_function(result, **kwargs))


    def speciation(self):
        for test_org in self._organisms:
            assigned = False
            for org in self._organisms:
                if org.species() is not None and gens.sigma(test_org.genome(), org.genome()) < sigma_threshold:
                    assigned = True
                    org.species().representatives().append(test_org)
                    test_org.assign_to_species(org.species())
                if assigned:
                    break
            if not assigned:
                species = Species(self._species_number)
                species.representatives().append(test_org)
                test_org.assign_to_species(species)
                self._species.append(species)
                self._species_number += 1


    def eliminate(self):
        for species in self._species:
            if len(species.representatives()) > 1:
                to_eliminate = species.representatives()[0]
                for rep in species.representatives():
                    if rep.score() < to_eliminate.score():
                        to_eliminate = rep
                self._organisms.remove(to_eliminate)
                species.representatives().remove(to_eliminate)




    def mutate(self):
        for org in self._organisms:
            org.mutate()


    def crossover(self):
        pass


    def start_simulation(self, solve_task, reward_function, first=False, input_neurons=0, output_neurons=1, **kwargs):
        self.spawn(first=first, input_neurons=input_neurons, output_neurons=output_neurons)
        self.evaluate(solve_task, reward_function, **kwargs)
        self.speciation()
        self.eliminate()
        self.mutate()
        self.crossover()



    """ HELPERS """
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

    def species_number(self):
        return self._species_number

    def species(self):
        return self._species
