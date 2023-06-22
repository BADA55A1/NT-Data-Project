import networkx as nx
import matplotlib.pyplot as plt

def get_edge_to_node(nodes_raw, edges_raw):
    nodes_c = len(nodes_raw)
    edges_c = len(edges_raw)
    return edges_c/nodes_c

def get_num_sub_sinks(nodes_raw, edges_raw):
    out_edges_per_node = [[] for i in nodes_raw]
    for i, node in enumerate(nodes_raw):
        for edge in edges_raw:
            if edge.from_node == node:
                out_edges_per_node[i].append(edge)
    #check_if_subsink
    subsinks = []
    for i, _ in enumerate(out_edges_per_node):
        is_subsink = True
        for edge in out_edges_per_node[i]:
            if edge.to_node.fitness() > edge.from_node.fitness():
                is_subsink = False
        if is_subsink:
            subsinks.append(i)
    return len(subsinks)


def save_graph(nodes_raw, edges_raw, name):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes
    nodes = [i for i in enumerate(nodes_raw)]
    edges = [(
        nodes_raw.index(edge.from_node),
        nodes_raw.index(edge.to_node),
        {"weight": edge.weight}
    ) for edge in edges_raw]
    G.add_nodes_from(nodes)

    # Add edges with values
    G.add_edges_from(edges)

    # Plot the graph
    pos = nx.spring_layout(G)  # Layout algorithm for node positioning
    nx.draw_networkx_nodes(G, pos, node_color='r', node_size=50)
    nx.draw_networkx_edges(G, pos, edge_color='b', width=2)

    # Draw edge labels
    labels = {g_node: f"{i}: {int(node.fitness())}" for (i, node), g_node in zip(enumerate(nodes_raw), G.nodes())}  # Convert nodes to string labels
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

    e_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=e_labels)

    # Customize the plot
    plt.title("Graph with Edge Values")

    # Display the plot
    plt.axis('off')  # Turn off the axis labels
    plt.savefig(f"img/{name}.png")
    plt.close()
