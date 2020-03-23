import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

colors = ['Red', 'Blue', 'Green', 'Yellow']

G.add_nodes_from(["Guyane French","Suriname","Guyane","Venezuela","Columbia","Ecuador","Peru","Bolivia","Paraguay","Uruguay","Argentina","Chile","Brazil"])
G.add_edges_from([(1,12),(0,2,12),(1,3,12),(2,4,12),(3,5,8,12),(4,6),(5,7,12),(6,8,10,11,12),(7,10,12),(10,12),(7,8,9,11,12),(6,7,10),(0,1,2,3,4,6,7,8,9,10)])
colors_of_nodes={}


def coloring(node, color):
   for neighbor in G.neighbors(node):
       color_of_neighbor = colors_of_nodes.get(neighbor, None)
       if color_of_neighbor == color:
          return False

   return True

def get_color_for_node(node):
    for color in colors:
       if coloring(node, color):
          return color

def main():
    for node in G.nodes():
        colors_of_nodes[node] = get_color_for_node(node)

    print(colors_of_nodes)


main()
