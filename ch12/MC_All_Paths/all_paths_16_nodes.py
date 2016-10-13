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
    "1": ("2", "3", "6", "9"),
    "2": ("3", "4", "8", "9", "12", "14", "15", "16"),
    "3": ("1", "10", "11", "16"),
    "4": ("1", "2", "5", "6", "7", "8", "10", "11", "13", "16"),
    "5": ("2", "7", "10", "11", "15"),
    "6": ("1", "9", "12"),
    "7": ("4", "6", "9", "14", "16"),
    "8": ("1", "9", "10", "11", "14"),
    "9": ("1", "2", "5", "11", "14"),
    "10": ("1", "2", "5", "6", "9", "13", "15"),
    "11": ("3", "4", "5", "6", "8", "11", "13", "14", "16"),
    "12": ("3", "10", "16"),
    "13": ("1", "2", "5", "6", "14"),
    "14": ("3", "5", "6", "7", "9", "12", "15"),
    "15": ("1", "12", "13", "16"),
    "16": ("1", "2", "4", "8", "11"),
}

paths = find_all_paths(graph, "1", "16")

print("Number of Paths = ", len(paths))
