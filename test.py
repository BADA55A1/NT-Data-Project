#!/usr/bin/env python
# import matplotlib.pyplot as plt
import os

import ts_problem
import lon
import networkx as nx
import matplotlib.pyplot as plt

# print(p.distances)
import utils

'''
sol = ts_problem.TSSolution(p)
# print(sol.s)
# print(sol.fitness())

sol2 = ts_problem.TSSolution(p)
# print(sol == sol2)

# test neighbour
test_sol = ts_problem.TSSolution(p, neighbourhood_fn=ts_problem.neighbourhood_fn)
test_neighbors = test_sol.get_neighbors()

print("test neighbors")
print(test_sol.s.tolist())
print([i.s.tolist() for i in test_neighbors])
print("test opt")
print(f"before result {test_sol.fitness()}")
print(test_sol.get_2_opt())
print(f"min result {test_sol.fitness()}")

print("test opt")
print(f"before result {test_sol.fitness()}")
print(test_sol.get_2_opt())
print(f"min result {test_sol.fitness()}")
'''


class TSSolutionWithSimpleNeighbour(ts_problem.TSSolution):
    def __init__(self, problem, solution=None, neighbourhood_fn=ts_problem.neighbourhood_fn_2_opt):
        super().__init__(problem,
                         solution=solution, neighbourhood_fn=neighbourhood_fn)


datafiles = ['ulysses16.tsp']  # , 'ulysses22.tsp']#os.listdir('data/2d')

for f in datafiles:
    print('running for %s...' % f)
    p = ts_problem.TSProblem('./data/2d/' + f)

    l = lon.LON(p, TSSolutionWithSimpleNeighbour)
    print("generating nodes")
    l.generate_nodes(10, 10)

    print("generating edges")
    l.generate_edges(10)

    print('edges:')
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
    utils.plot_graph(l.nodes, l.edges)

'''
def node_to_int(node):
    int_value = 0
    pow = 0
    for i in node.s:
        int_value += float(i) * p.size ** pow
        pow += 1
    return int_value


def print_fittnes_landscape():
    nodes = l.nodes
    o_nodes = l.nodes
    neighbour_points = [i for node in l.nodes for i in node.get_neighbors()]
    for d in range(1, 9):
        neighbour_points.extend([i for node in l.nodes for i in node.get_deep_neighbours(d)])

    nodes = [*nodes, *neighbour_points]
    values = [i.fitness() for i in nodes]
    o_values = [i.fitness() for i in o_nodes]

    nodes = [node_to_int(i) for i in nodes]
    o_nodes = [node_to_int(i) for i in o_nodes]

    nodes, values = (list(t) for t in zip(*sorted(zip(nodes, values))))

    plt.figure()
    plt.plot(nodes, values)
    plt.plot(o_nodes, o_values, '*')
    #plt.xscale('log', base=p.size)
    plt.show()


# print_fittnes_landscape()
'''




