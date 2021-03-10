"""This file introduces all operations that could be done with 2 Genomes (Neural Networks)"""

from genome.Genome import Genome
from config import c1, c2, c3


"""Given 2 parents a particular offspring will come out"""
def produce_offspring(genome_1: Genome, genome_2: Genome):
    pass



"""Determines how 'far' 2 Genomes are (helps to assign different Genomes to different Species)"""
def sigma(genome_1: Genome, genome_2: Genome):

    N = _set_N(genome_1, genome_2)
    E, D = _excesses_disjoints(genome_1, genome_2)
    W = _weights_differences_avg(genome_1, genome_2)

    return c1 * E/N + c2 * D/N + c3 * W


""" HELPERS """

def _excesses_disjoints(genome_1: Genome, genome_2: Genome):
    E = 0
    D = 0
    last_gene = pick_last_disjoint_gene(genome_1, genome_2)

    for con in genome_1.connections().extend(genome_2.connections()):
        if con not in genome_1 or con not in genome_2:
            if con.innovation_number() <= last_gene:
                D += 1
            else:
                E += 1
    return E, D


def _weights_differences_avg(genome_1: Genome, genome_2: Genome) -> int:
    pass


def _set_N(genome_1, genome_2) -> int:
    pass


def pick_last_disjoint_gene(genome_1, genome_2):
    for con in genome_1.connections()[::-1]:
        if con not in genome_2.connections():
            return con.innovation_number()

    # Return the last gene's innovation number in genome_1
    # in case every gene matched with genome_2 genes
    return genome_1.connections()[-1].innovation_number() + 1
