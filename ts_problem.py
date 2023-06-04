import random
from typing import List

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

    def __hash__(self):
        return hash((self.problem, str(self.s)))

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
    def get_neighbors(self) -> List['TSSolution']:
        return self.neighbourhood_fn(self)

    # checks if solution is better than it's neighbors [bool]
    def is_local_optimum(self):
        this_fitness = self.fitness()
        for n_sol in self.get_neighbors():
            if this_fitness > n_sol.fitness():
                return False
        return True

    def get_deep_neighbours(self, search_depth):
        neighbor_list = [self]
        for i in range(search_depth):
            new_neighbor = [j.get_neighbors() for j in neighbor_list]
            neighbor_list = [item for sublist in new_neighbor for item in sublist]
            # filter duplicates
            neighbor_list = list(set(neighbor_list))
        return neighbor_list

    # perform a 2-opt solution optimization
    def get_2_opt(self, search_depth=1):
        optimum = self
        while not optimum.is_local_optimum():
            neighbor_list = optimum.get_deep_neighbours(search_depth)
            solutions_fitness = [i.fitness() for i in neighbor_list]
            min_fitness = min(solutions_fitness)
            if min_fitness < optimum.fitness():
                index_of_min_fitness = solutions_fitness.index(min_fitness)  # TODO not efficient
                optimum = neighbor_list[index_of_min_fitness]
        return optimum

    # perform a simplifyed 2-opt solution optimization
    # (first-improving move is chosen)
    def get_1st_impr_2_opt(self, search_depth=1):
        optimum = self
        while not optimum.is_local_optimum():
            neighbor_list = optimum.get_deep_neighbours(search_depth)
            for i in neighbor_list:
                if i.fitness() < optimum.fitness():
                    optimum = i
            # otherwise
        return optimum

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
