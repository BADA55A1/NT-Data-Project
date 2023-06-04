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
	def __init__(self, problem, solution = None):
		self.problem = problem
		if solution is None:
			self.s = np.arange(self.problem.size)
			np.random.shuffle(self.s)
		else:
			self.s = solution
	
	# checks if solution is equal to another
	def __eq__(self, other):
		return (self.problem is other.problem) and (self.s == other.s).all()

	# Quality function (less == better), Real number [float/int]
	def fitness(self):
		path_distance = 0
		for i in range(self.problem.size):
			path_distance += self.problem.distances[self.s[i-1]][self.s[i]]
		return path_distance

	# returns a list of 2-change neighbor solutions [list<Solution>]
	def get_neighbors(self):
		return []

	# checks if solution is better than it's neighbors [bool]
	def is_local_optimum(self):
		this_fitness = self.fitness()
		for n_sol in self.get_neighbors():
			if this_fitness < n_sol.fitness():
				return False
		return True

	# perform a 2-opt solution optimization
	def apply_2_opt(self):
		pass

	# perform a simplifyed 2-opt solution optimization 
	# (first-improving move is chosen)
	def apply_1st_impr_2_opt(self):
		apply_2_opt(self)

	# perform two random 2-change moves performed one-by-one
	def apply_random_kick(self):
		for _ in range(2): # 2 moves
			# swap nearest in list
			place = np.random.randint(self.problem.size)
			self.s[place-1], self.s[place] = self.s[place], self.s[place-1]
		
			# alternative: swap two random ones
			place_a = np.random.randint(self.problem.size)
			place_b = place_a
			while place_b == place_a:
				place_b = np.random.randint(self.problem.size)
			self.s[place_a], self.s[place_b] = self.s[place_b], self.s[place_a]


