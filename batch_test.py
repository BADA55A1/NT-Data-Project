#!/usr/bin/env python
# import matplotlib.pyplot as plt
import os

import ts_problem
import lon
import utils



datafiles = ['ulysses16.tsp', 'ulysses22.tsp']

for f in datafiles:
    print('running for %s...' % f)
    p = ts_problem.TSProblem('./data/2d/' + f)

    l = lon.LON(p, ts_problem.TSSolutionWithSimpleNeighbour)
    print("generating nodes")
    l.generate_nodes(100, 10)

    print("generating edges                    ")
    l.generate_edges(10)

    print('edges:                              ')
    for edge in l.edges:
        if edge.from_node != edge.to_node:
            print(
                '  E(%d, %d), weight: %d' %
                (
                    l.nodes.index(edge.from_node),
                    l.nodes.index(edge.to_node),
                    edge.weight
                )
            )
    utils.save_graph(l.nodes, l.edges, f)
    print(f"Edge to node: {utils.get_edge_to_node(l.nodes, l.edges)}")
    print(f"Subsinks: {utils.get_num_sub_sinks(l.nodes, l.edges)}")
    print(f"escRate: {l.escRate}")
