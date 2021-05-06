"""This file introduces all operations that could be done with 2 Genomes (Neural Networks)"""

from genome.Genome import Genome
from genome.util.Status import Status
from config import c1, c2, c3, disable_connection_chance

import numpy as np
import random


"""Given 2 parents a particular offspring will come out"""
def produce_offspring(generation, genome_1: Genome, genome_2: Genome) -> Genome:

    offspring = Genome(generation, genome_1.input_nodes(), genome_1.output_nodes(), connections=False)
    # TMP
    offspring.offspringed()
    #

    for node in genome_1.nodes() + genome_2.nodes():
        if node not in offspring.nodes():
            offspring.nodes().append(node.copy_without_connections())


    # all common genes are appended randomly from either parent
    for con in genome_1.connections():
        if con in genome_2.connections():
            index = genome_2.connections().index(con)
            gene = _pick_random_gene(con, genome_2.connections()[index])
            _append_con(gene, offspring)


    for con in genome_1.connections() + genome_2.connections():
        if (con in offspring.connections()) and (con.status() == Status.DISABLED):
            for in_con in offspring.connections():
                if in_con == con and in_con.status() == Status.ENABLED:
                    if _disable_chance():
                        in_con.disable()
                    break
        elif con not in offspring.connections():
            if (con.status() == Status.DISABLED) and (not _disable_chance()):
                con.enable()

            _append_con(con, offspring)


    return offspring


def _disable_chance():
    chance = random.uniform(0, 1)
    return chance <= disable_connection_chance


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


def _pick_random_gene(con1, con2):
    if random.uniform(0, 1) > 0.5:
        return con2
    return con1


def _append_con(con, offspring):
    input_node = offspring.nodes()[offspring.nodes().index(con.input_node())]
    output_node = offspring.nodes()[offspring.nodes().index(con.output_node())]

    con = con.copy_con(input_node, output_node)
    con.input_node().connections_out().append(con)
    con.output_node().connections_in().append(con)

    offspring.connections().append(con)
