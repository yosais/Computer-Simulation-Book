def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
   # if start not in graph:
     #   return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    

graph = {
    "1": ("2", "4"),
    "2": ("1", "4", "5"),
    "3": ("4", "5"),
    "4": ("1", "2", "3"),
    "5": ("2", "3"),
}

paths = find_all_paths(graph, "1", "5")

print("Number of Paths = ", len(paths))

for path in paths:
	print(path)
