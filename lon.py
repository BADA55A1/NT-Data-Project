import numpy as np

class Edge:
	pass

class LON:
	def __init__(self, problem, solution_type):
		self.problem = problem
		self.Solution = solution_type
		self.nodes = []
		self.node_edge_map = None

	def generate_nodes(self, I_nodes, I_attempts):
		for i_n in range(I_nodes):
			for i_a in range(I_attempts):
				print('generating node %d, attempt %d' % (i_n, i_a), end='\r')

				s = self.Solution(self.problem)
				s = s.apply_2_opt()
				if s.is_local_optimum() and not(s in self.nodes):
					self.nodes.append(s)
					break
		print()

	def generate_edges(self, I_edges):
		self.node_edge_map = np.zeros((len(self.nodes), len(self.nodes)))
		for node in self.nodes:
			kick_moves = I_edges
			while kick_moves > 0:

				n = node.copy()
				n = n.apply_random_kick()
				n = n.apply_1st_impr_2_opt()
				
				if n in self.nodes:
					kick_moves -= 0
					self.node_edge_map[self.nodes.index(node)][self.nodes.index(n)] += 1
					#ToDo Edges



