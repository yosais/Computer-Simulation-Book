from copy import deepcopy
import random as rnd

def update_adj_matrix(AdjMat, current):
	for node in AdjMat:
		neighbors = AdjMat[node]
		new_neighbors = ()
		for n in neighbors:
			if n != current:
				new_neighbors = new_neighbors + (n,)
		AdjMat[node] = new_neighbors
	return AdjMat


def monte_carlo(source, destination, AdjMat, N):
	paths = []
	for i in range(N):
		# Clone the AdjMat
		_AdjMat = deepcopy(AdjMat)

		x = [source]
		g = 1
		current = source

		# Remove current from being a potential next node
		update_adj_matrix(_AdjMat, current)
	
		while current != destination:
			# Get set of possible next nodes
			V = _AdjMat[current]

			# Check if V is empty
			if len(V) == 0: break

			# Choose next node
			next = rnd.choice(V)
			x.append(next)

			# Step 5
			current = next
			update_adj_matrix(_AdjMat, current)
			g = g / len(V)

		# Store the path and its g
		if x[ len(x)-1 ] == destination:
			paths.append((x, g))

	return paths


graph = {
    "1": ("2", "3", "4", "6", "7", "8"),
    "2": ("1", "5", "6", "7"),
    "3": ("1", "4", "5", "6", "7", "8"),
    "4": ("1", "3", "5", "6", "7", "8"),
    "5": ("2", "3", "4", "6"),
    "6": ("1", "2", "3", "4", "5", "7", "8"),
    "7": ("1", "2", "3", "4", "6", "8"),
    "8": ("1", "3", "4", "6", "7"),
}


paths = monte_carlo("1", "8", graph, 10)

estimate = 0
for (path, g) in paths:
	estimate = estimate + 1/g
	print(path, " -> ", g)

estimate = estimate / len(paths)

print("\nEstimate = ", round(estimate, 2))