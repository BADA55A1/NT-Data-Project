#!/usr/bin/env python

import ts_problem

p = ts_problem.TSProblem(10, 1, 40, dtype=int)
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

import lon


class TSSolutionWithSimpleNeighbour(ts_problem.TSSolution):
    def __init__(self, problem, solution=None, neighbourhood_fn=ts_problem.neighbourhood_fn):
        super.__init__(self, problem,
                       solution=solution, neighbourhood_fn=neighbourhood_fn)


l = lon.LON(p, TSSolutionWithSimpleNeighbour)
l.generate_nodes(10, 10)

for n in l.nodes:
    print(n.s)
