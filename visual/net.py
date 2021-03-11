from graphviz import Digraph
from genome.Genome import Genome


def construct(genome: Genome):
    dot = Digraph()
    for node in genome.nodes():
        dot.node(str(node.innovation_number()), str(node.innovation_number()))
    for con in genome.connections():
        dot.edge(str(con.input_node().innovation_number()), str(con.output_node().innovation_number()))
    dot.render('/Users/max/IdeaProjects/neat/network_pictures/net', view=True)
