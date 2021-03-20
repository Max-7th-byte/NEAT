from graphviz import Digraph
from genome.Genome import Genome
from genome.util.Status import Status


def construct(genome: Genome, file_name):
    dot = Digraph()
    for node in genome.nodes():
        dot.node(str(node.id()), str(node.id()))
    for con in genome.connections():
        if con.status() == Status.ENABLED:
            dot.edge(str(con.input_node().id()), str(con.output_node().id()))
    dot.render(f'/Users/max/IdeaProjects/neat/network_pictures/{file_name}', view=True)
