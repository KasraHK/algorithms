def dfs(v):
    global color
    color = {}
    global time
    time = 0
    global discovery_time
    discovery_time = {}
    global finish_time
    finish_time = {}
    global visited_by
    visited_by = {}
    for vertice in v:
        color[vertice] = 'white'
    for vertice in v:
        if color[vertice] == 'white':
            dfs_visit(vertice)
    
def dfs_visit(ver):
    global time
    color[ver] = 'gray'
    time += 1
    discovery_time[ver] = time
    for neighbour in neighbours[ver]:
        if color[neighbour] == 'white':
            visited_by[neighbour] = ver
            dfs_visit(neighbour)
    color[ver] = 'black'
    finish_time[ver] = time
    
# Example usage
v = 'a b c d e f g h i'.split()
global neighbours
neighbours = {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'd'], 'd': ['b', 'c', 'e'], 'e': ['b', 'd', 'f', 'i', 'h'], 'f': ['e', 'g'], 'g': ['f'], 'h': ['i', 'e'], 'i':['h', 'e']}
dfs(v)
print(discovery_time, '\n', finish_time)