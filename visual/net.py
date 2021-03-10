from graphviz import Digraph
from genome.Genome import Genome


def construct(genome: Genome):
    dot = Digraph()
    for node in genome.nodes():
        dot.node(str(node.id()), str(node.id()))
    for con in genome.connections():
        dot.edge(str(con.input_node().id()), str(con.output_node().id()))
    dot.render('/Users/max/IdeaProjects/neat/network_pictures/net', view=True)
