#!/usr/bin/env python
import matplotlib.pyplot as plt

import ts_problem

p = ts_problem.TSProblem(5, 1, 40, dtype=int)
print(p.distances)

sol = ts_problem.TSSolution(p)
print(sol.s)
print(sol.fitness())

sol2 = ts_problem.TSSolution(p)
print(sol == sol2)

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

import lon


class TSSolutionWithSimpleNeighbour(ts_problem.TSSolution):
    def __init__(self, problem, solution=None, neighbourhood_fn=ts_problem.neighbourhood_fn):
        super().__init__(problem,
                         solution=solution, neighbourhood_fn=neighbourhood_fn)


l = lon.LON(p, TSSolutionWithSimpleNeighbour)
print("generating nodes")
l.generate_nodes(5, 10)
print("generated nodes")

# for n in l.nodes:
#     print(n.s)

print("generating edges")
l.generate_edges(10)

def node_to_int(node):
    int_value = 0
    pow = 0
    for i in node.s:
        int_value += float(i)*10.0**pow
        pow+=1
    return int_value

def print_fittnes_landscape():
    nodes = l.nodes
    o_nodes = l.nodes
    nodes_of_nodes = [i for node in l.nodes for i in node.get_neighbors()]
    nodes_of_nodes_2 = [i for node in l.nodes for i in node.get_deep_neighbours(2)]
    nodes_of_nodes_3 = [i for node in l.nodes for i in node.get_deep_neighbours(3)]

    nodes = [*nodes, *nodes_of_nodes, *nodes_of_nodes_2, *nodes_of_nodes_3]
    values = [i.fitness() for i in nodes]
    o_values = [i.fitness() for i in o_nodes]

    nodes = [node_to_int(i) for i in nodes]
    o_nodes = [node_to_int(i) for i in o_nodes]

    nodes, values = (list(t) for t in zip(*sorted(zip(nodes, values))))

    plt.figure()
    plt.plot(nodes, values)
    plt.plot(o_nodes, o_values, '*')
    plt.show()

print_fittnes_landscape()
