#!/usr/bin/env python

import ts_problem

p = ts_problem.TSProblem(10, 1, 40, dtype=int)
print(p.distances)

sol = ts_problem.TSSolution(p)
print(sol.s)
print(sol.fitness())