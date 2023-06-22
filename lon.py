import numpy as np

class Edge:
	def __init__(self, from_node, to_node):
		self.from_node = from_node
		self.to_node = to_node
		self.weight = 1

	def __eq__(self, other):
		return (self.from_node == other.from_node) and (self.to_node == other.to_node)

	def weight_increment(self):
		self.weight += 1


class LON:
	def __init__(self, problem, solution_type):
		self.problem = problem
		self.Solution = solution_type
		self.nodes = []
		self.node_edge_map = None
		self.edges = []
		self.connections_to_undefined_nodes = 0

	def generate_nodes(self, I_nodes, I_attempts):
		for i_n in range(I_nodes):
			for i_a in range(I_attempts):
				print('generating node %d, attempt %d' % (i_n, i_a), end='\r')

				s = self.Solution(self.problem)
				s = s.get_2_opt()
				if s.is_local_optimum() and not(s in self.nodes):
					self.nodes.append(s)
					break
		print()

	def generate_edges(self, I_edges):
		self.node_edge_map = np.zeros((len(self.nodes), len(self.nodes)))
		for node in self.nodes:
			kick_moves = 2
			i = I_edges
			while i > 0:
				i -= 1

				n = node.copy()
				n = n.get_random_kick(kick_moves)
				n = n.get_1st_impr_2_opt()

				if n in self.nodes:
					if node != n:
						print(
							'found edge s(%d, %d), kick moves: %d' %
							(self.nodes.index(node), self.nodes.index(n), kick_moves)
						)
						self.node_edge_map[self.nodes.index(node)][self.nodes.index(n)] += 1

						# Edge class
						edge = Edge(node, n)
						if edge in self.edges:
							self.edges[self.edges.index(edge)].weight_increment()
						else:
							self.edges.append(edge)
				else:
					self.connections_to_undefined_nodes += 1




