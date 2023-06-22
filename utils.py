import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# Add edges with values
edges = [(1, 2, {'weight': 10}), (2, 3, {'weight': 7}), (3, 4, {'weight': 5}),
         (4, 5, {'weight': 3}), (5, 1, {'weight': 8})]
G.add_edges_from(edges)

# Plot the graph
pos = nx.spring_layout(G)  # Layout algorithm for node positioning
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='b', width=2)

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Customize the plot
plt.title("Graph with Edge Values")

# Display the plot
plt.axis('off')  # Turn off the axis labels
plt.show()
