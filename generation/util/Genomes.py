"""This file introduces all operations that could be done with 2 Genomes (Neural Networks)"""

from genome.Genome import Genome
from genome.util.Status import Status
from generation.Generation import Generation
from config import c1, c2, c3
import copy

import numpy as np


"""Given 2 parents a particular offspring will come out"""
def produce_offspring(generation: Generation, genome_1: Genome, genome_2: Genome) -> Genome:

    offspring = Genome(generation, genome_1.input_nodes(), genome_1.output_nodes(), connections=False)

    for node in genome_1.nodes() + genome_2.nodes():
        if node not in offspring.nodes():
            offspring.nodes().append(node.copy_without_connections())

    for con in genome_1.connections() + genome_2.connections():
        if (con in offspring.connections()) and (con.status() == Status.DISABLED):
            for i, in_con in enumerate(offspring.connections()):
                if in_con == con:
                    in_con.disable()
                    break
        elif con not in offspring.connections():
            offspring.connections().append(con)


    return offspring




"""Determines how 'far' 2 Genomes are (helps to assign different Genomes to different Species)"""
def sigma(genome_1: Genome, genome_2: Genome):

    N = _set_N(genome_1, genome_2)
    E, D = _excesses_disjoints(genome_1, genome_2)
    W = _weights_differences_avg(genome_1, genome_2)

    return c1 * E/N + c2 * D/N + c3 * W


""" HELPERS """

# TODO: I can improve counting excesses and disjoints by not looking for max in 1st parent
#  but remembering the last disjoint in 1st parent and then tweaking E and D properly
def _excesses_disjoints(genome_1: Genome, genome_2: Genome):
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

    for con_1 in genome_1.connections():
        for con_2 in genome_2.connections():
            if con_1 == con_2:
                diff += np.abs(con_1.weight() - con_2.weight())
    return diff



def _set_N(genome_1, genome_2) -> int:
    N = (genome_1.size() + genome_2.size()) // 20
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
