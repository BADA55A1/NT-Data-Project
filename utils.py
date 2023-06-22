import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(nodes_raw, edges_raw):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes
    nodes = [i for i in enumerate(nodes_raw)]
    edges = [(
        nodes_raw.index(edge.from_node),
        nodes_raw.index(edge.to_node),
        {"weight": edge.weight}
    ) for edge in enumerate(edges_raw)]
    G.add_nodes_from(nodes)

    # Add edges with values
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
