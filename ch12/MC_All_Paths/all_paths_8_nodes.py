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
    "1": ("2", "3", "4", "6", "7", "8"),
    "2": ("1", "5", "6", "7"),
    "3": ("1", "4", "5", "6", "7", "8"),
    "4": ("1", "3", "5", "6", "7", "8"),
    "5": ("2", "3", "4", "6"),
    "6": ("1", "2", "3", "4", "5", "7", "8"),
    "7": ("1", "2", "3", "4", "6", "8"),
    "8": ("1", "3", "4", "6", "7"),
}

paths = find_all_paths(graph, "1", "8")

print("Number of Paths = ", len(paths))

