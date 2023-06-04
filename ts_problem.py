import random

import numpy as np
import copy

import problem
import neighbourhood

DISTANCE_DEF_DATA_TYPE = int  # or float


class TSProblem(problem.Problem):
    # Generates random TS problem distances, range [d_min, d_max],
    #   based on given cities number (size)
    def __init__(self, size, d_min, d_max, dtype=DISTANCE_DEF_DATA_TYPE):
        self.size = size
        self.distances = np.random.randint(
            d_min,
            d_max,
            (size, size),
            dtype=dtype
        )
        for i in range(size):
            self.distances[i][i] = 0


class TSSolution(problem.Solution):
    # Generates random solution based on problem
    def __init__(self, problem, solution=None, neighbourhood_fn=None):
        self.problem = problem
        self.neighbourhood_fn = neighbourhood_fn
        if solution is None:
            self.s = np.arange(self.problem.size)
            np.random.shuffle(self.s)
        else:
            self.s = solution

    # checks if solution is equal to another
    def __eq__(self, other):
        return (self.problem is other.problem) and (self.s == other.s).all()

    def copy(self):
        return TSSolution(
            self.problem,
            copy.deepcopy(self.s),
            self.neighbourhood_fn
        )

    # Quality function (less == better), Real number [float/int]
    def fitness(self):
        path_distance = 0
        for i in range(self.problem.size):
            path_distance += self.problem.distances[self.s[i - 1]][self.s[i]]
        return path_distance

    # returns a list of 2-change neighbor solutions [list<TSSolution>]
    def get_neighbors(self):
        return self.neighbourhood_fn(self)

    # checks if solution is better than it's neighbors [bool]
    def is_local_optimum(self):
        this_fitness = self.fitness()
        for n_sol in self.get_neighbors():
            if this_fitness < n_sol.fitness():
                return False
        return True

    # perform a 2-opt solution optimization
    def get_2_opt(self):  # TODO write that it's simplified (just one step)
        neighbors = self.get_neighbors()
        solutions_fitness = [i.fittness() for i in neighbors]
        max_fitness = max(solutions_fitness)
        if max_fitness > self.fitness():
            index_of_max_fitness = solutions_fitness.index(max_fitness)  # TODO not efficient
            return neighbors[index_of_max_fitness]
        else:
            return self

    # perform a simplifyed 2-opt solution optimization
    # (first-improving move is chosen)
    def apply_1st_impr_2_opt(self):
        neighbors = self.get_neighbors()
        for i in neighbors:
            if i.fittness() > self.fitness():
                return i
        # otherwise
        return self

    # perform two random 2-change moves performed one-by-one


def get_random_kick(self, number_of_kicks=2):
    new_el = self
    for i in range(number_of_kicks):
        new_el = random.choice(new_el.get_neighbors())
    return new_el


def neighbourhood_fn(ts_solution: TSSolution):
    first_element = int(ts_solution.s.tolist()[0])
    raw_solutions = neighbourhood.dim_1_neighbourhood(
        ts_solution.s.tolist()[1:])  # removing 1st el
    raw_solutions = [[first_element, *no_first_el_solution] for no_first_el_solution in raw_solutions if
                     no_first_el_solution is not None]

    neighbour_solutions = [TSSolution(problem=ts_solution.problem, solution=np.asarray(raw_solution),
                                      neighbourhood_fn=ts_solution.neighbourhood_fn) for raw_solution
                           in raw_solutions]
    return neighbour_solutions
