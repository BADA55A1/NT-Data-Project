
class LON:
	def __init__(self, problem, solution_type):
		self.problem = problem
		self.Solution = solution_type
		self.nodes = []

	def generate_nodes(self, I_nodes, I_attempts):
		for i_n in range(I_nodes):
			for i_a in range(I_attempts):
				print('generating node %d, attempt %d' % (i_n, i_a), end='\r')

				s = self.Solution(self.problem)
				s.apply_2_opt()
				if s.is_local_optimum() and not(s in self.nodes):
					self.nodes.append(s)
					break
		print()

