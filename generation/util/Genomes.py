"""This file introduces all operations that could be done with 2 Genomes (Neural Networks)"""

from genome.Genome import Genome
from generation.Generation import Generation
from config import c1, c2, c3
import copy

import numpy as np


"""Given 2 parents a particular offspring will come out"""
def produce_offspring(generation: Generation, genome_1: Genome, genome_2: Genome) -> Genome:

    offspring = Genome(generation, genome_1.input_nodes(), genome_1.output_nodes(), connections=False)

    for node in genome_1.nodes() + genome_2.nodes():
        if node not in offspring.nodes():
            offspring.nodes().append(copy.deepcopy(node))

    for con in genome_1.connections() + genome_2.connections():
        if con not in offspring.connections():
            offspring.connections().append(con)

    return offspring




"""Determines how 'far' 2 Genomes are (helps to assign different Genomes to different Species)"""
def sigma(genome_1: Genome, genome_2: Genome):

    N = _set_N(genome_1, genome_2)
    E, D = excesses_disjoints(genome_1, genome_2)
    W = _weights_differences_avg(genome_1, genome_2)

    return c1 * E/N + c2 * D/N + c3 * W


""" HELPERS """

# TODO: I can improve counting excesses and disjoints by not looking for max in 1st parent
#  but remembering the last disjoint in 1st parent and then tweaking E and D properly
def excesses_disjoints(genome_1: Genome, genome_2: Genome):
    E = 0
    D = 0
    last_disjoint = _pick_last_disjoint_connection(genome_1, genome_2)

    for con in genome_1.connections() + genome_2.connections():
        if con not in genome_1.connections() or con not in genome_2.connections():
            if con.innovation_number() <= last_disjoint:
                D += 1
            else:
                E += 1
    return E, D


def _weights_differences_avg(genome_1: Genome, genome_2: Genome) -> float:
    diff = 0

    cur_innov_number = 0
    ind_1 = 0
    ind_2 = 0
    length = _pick_last_disjoint_connection(genome_1, genome_2)

    while cur_innov_number < length:

        innov_1 = genome_1.connections()[ind_1].innovation_number()
        innov_2 = genome_2.connections()[ind_2].innovation_number()

        if innov_1 == innov_2:
            diff += np.abs(genome_1.connections()[ind_1].weight() - genome_2.connections()[ind_2].weight())
            ind_1 += 1
            ind_2 += 1
        elif innov_1 > innov_2:
            ind_2 += 1
        else:
            ind_1 += 1

        cur_innov_number += 1
    return diff



def _set_N(genome_1, genome_2) -> int:
    N = (len(genome_1.size()) + len(genome_2.size())) // 20
    if N <= 1:
        return 1
    return N


def _pick_last_disjoint_connection(genome_1, genome_2):
    for con in genome_1.connections()[::-1]:
        if con not in genome_2.connections():
            return con.innovation_number()

    # Return the last connection's innovation number in genome_1
    # in case every gene matched with genome_2 genes
    return genome_1.connections()[-1].innovation_number()


def _pick_last_disjoint_node(genome_1, genome_2):
    for node in genome_1.nodes()[::-1]:
        if node not in genome_2.nodes():
            return node.innovation_number()

    # Return the last node's innovation number in genome_1
    # in case every gene matched with genome_2 genes
    return genome_1.nodes()[-1].innovation_number() + 1
