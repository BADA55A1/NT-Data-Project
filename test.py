#!/usr/bin/env python

import ts_problem

p = ts_problem.TSProblem(10, 1, 40, dtype=int)
print(p.distances)

sol = ts_problem.TSSolution(p)
print(sol.s)
print(sol.fitness())

sol2 = ts_problem.TSSolution(p)
print(sol == sol2)

import lon

l = lon.LON(p, ts_problem.TSSolution)
l.generate_nodes(10, 10)

for n in l.nodes:
	print(n.s)