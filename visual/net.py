from graphviz import Digraph
from genome.Genome import Genome

dot = Digraph()

def construct(genome: Genome):
    for node in genome.nodes():
        dot.node(str(node.id()), str(node.id()))
    for con in genome.connections():
        dot.edge(str(con.input_node().id()), str(con.output_node().id()))

construct(Genome(0, 3, 2))
dot.render('/Users/max/IdeaProjects/neat/network_pictures/net', view=True)
