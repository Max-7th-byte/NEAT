"""This file introduces all operations that could be done with 2 Genomes (Neural Networks)"""

from genome.Genome import Genome
from config import c1, c2, c3

_N = 1


"""Given 2 parents a particular offspring will come out"""
def produce_offspring(genome_1: Genome, genome_2: Genome):
    pass


"""Determines how 'far' 2 Genomes are (helps to assign different Genomes to different Species)"""
def genome_distance(genome_1: Genome, genome_2: Genome):

    N = _set_N(genome_1, genome_2)
    E = _excesses(genome_1, genome_2)
    D = _disjoints(genome_1, genome_2)

def _excesses(genome_1: Genome, genome_2: Genome) -> int:
    pass

def _disjoints(genome_1: Genome, genome_2: Genome) -> int:
    pass

def _weights_differences(genome_1: Genome, genome_2: Genome):
    pass


""" HELPERS """
def _set_N(genome_1, genome_2) -> int:
    pass
