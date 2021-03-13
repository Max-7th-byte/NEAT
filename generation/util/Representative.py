from generation.Species import Species
from genome.Genome import Genome

class Representative:


    def __init__(self, species: Species, genome: Genome):
        self._species = species
        self._genome = genome
        self._score = 0
