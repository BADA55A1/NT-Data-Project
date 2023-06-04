class Problem:
	pass

class Solution:
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