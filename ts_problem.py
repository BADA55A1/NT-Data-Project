import numpy as np

import problem

DISTANCE_DEF_DATA_TYPE = int # or float


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
	def __init__(self, problem):
		self._problem = problem

	# Quality function (less == better), Real number [float/int]
	def fitness(self):
		return 0 

	# returns a list of 2-change neighbor solutions [list<Solution>]
	def get_neighbors(self):
		return []

	# checks if solution is better than it's neighbors [bool]
	def is_local_optimum(self):
		return True

	# perform a 2-opt solution optimization
	def apply_2_opt(self):
		pass

	# perform a simplifyed 2-opt solution optimization 
	# (first-improving move is chosen)
	def apply_1st_impr_2_opt(self):
		pass

	# perform two random 2-change moves performed one-by-one
	def apply_random_kick(self):
		pass
