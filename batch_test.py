#!/usr/bin/env python
# import matplotlib.pyplot as plt
import os

import ts_problem
import lon
import utils



datafiles = ['ulysses16.tsp', 'ulysses22.tsp']

iterations = 10

for f in datafiles:
    print('Running for %s...' % f)
    edge_to_node = 0
    num_sub_sinks = 0
    escRate = 0
    for i in range(iterations):
        print('Batch iteration %d' % i)
        p = ts_problem.TSProblem('./data/2d/' + f)
        l = lon.LON(p, ts_problem.TSSolutionWithSimpleNeighbour)
        l.generate_nodes(100, 10)
        print("                                       \r", end='\r')
        l.generate_edges(10)
        print("                                       \r", end='\r')
        edge_to_node += utils.get_edge_to_node(l.nodes, l.edges)
        num_sub_sinks += utils.get_num_sub_sinks(l.nodes, l.edges)
        escRate += l.escRate

    print(f"Edge to node: {edge_to_node / iterations}")
    print(f"Subsinks: {num_sub_sinks / iterations}")
    print(f"escRate: {escRate / iterations}")
