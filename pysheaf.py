import pysheaf as ps
# Constant sheaf for a topological space A has all of its stalks leading back to A
def BuildConstantSheaf(G, dataDimension=1):
    #Construct a constant sheaf on a graph G with a given dataDimension
    shf=ps.Sheaf()
    # Add cells for each node in the graph
    for node in G.nodes():
        shf.AddCell(node, ps.Cell('vector',dataDimension=dataDimension))
    # Add cofaces for each edge in the graph
    for edge in G.edges():
        shf.AddCoface(edge[0],edge[1],ps.Coface('vector','vector',dataTools.LinearMorphism(np.eye(dataDimension))))
    return shf # BuildConstantSheaf

#NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
#Nodes can be "anything" (e.g., text, images, XML records)
import networkx as nx
