import timeit

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
    "1": ("2","3","4","5","6","7","9","10","11","12"),
    "2": ("1","3","4","5","6","7","8","9","10","11","12"),
    "3": ("1","2","4","5","6","7","8","9","11","12"),
    "4": ("1","2","3","5","6","7","8","9","10","12"),
    "5": ("1","2","3","6","7","8","10","11","12"),
    "6": ("1","2","3","4","5","7","8","9","10","11"),
    "7": ("1","2","3","4","5","6","8","9","10","11","12"),
    "8": ("1","2","3","4","5","6","7","9","10","11","12"),
    "9": ("1","2","3","4","5","6","7","8","10","11","12"),
    "10": ("1","2","3","4","5","6","7","8","9","11"),
    "11": ("1","2","3","4","5","6","7","8","9","10","12"),
    "12": ("1","2","3","4","5","6","7","8","9","10","11"),
}

start = timeit.default_timer()

paths = find_all_paths(graph, "1", "12")

stop = timeit.default_timer()

print("Number of Paths = ", len(paths))

print("Runtime = ", round(stop - start, 2), " seconds")
