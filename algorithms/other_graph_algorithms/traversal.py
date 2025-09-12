from data_structures.graph import Graph
from data_structures.queue import Queue


def dfs(graph: Graph):
    """Depth-first search with discovery/finish times and parents.

    Returns:
        color, d, f, parent
    """
    n = graph.n
    color = {u: 'white' for u in range(n)}
    d = {u: 0 for u in range(n)}
    f = {u: 0 for u in range(n)}
    parent = {u: None for u in range(n)}
    time = [0]

    def visit(u: int):
        color[u] = 'gray'
        time[0] += 1
        d[u] = time[0]
        for e in graph.neighbors(u):
            v = e.v
            if color[v] == 'white':
                parent[v] = u
                visit(v)
        color[u] = 'black'
        time[0] += 1
        f[u] = time[0]

    for u in range(n):
        if color[u] == 'white':
            visit(u)
    return color, d, f, parent


def dfs_plus(graph: Graph):
    """DFS with edge classification, SCC (for directed), articulation points, and bridges.

    Returns:
        result dict with keys: color, d, f, parent, edges, scc, articulation, bridges
    """
    n = graph.n
    color = {u: 'white' for u in range(n)}
    d = {u: 0 for u in range(n)}
    f = {u: 0 for u in range(n)}
    parent = {u: None for u in range(n)}
    time = [0]
    edges = { 'tree': [], 'back': [], 'forward': [], 'cross': [] }
    low = {u: 0 for u in range(n)}
    articulation = set()
    bridges = []

    order = []

    def visit(u: int, root=False):
        color[u] = 'gray'
        time[0] += 1
        d[u] = low[u] = time[0]
        children = 0
        for e in graph.neighbors(u):
            v = e.v
            if color[v] == 'white':
                edges['tree'].append((u, v))
                parent[v] = u
                children += 1
                visit(v)
                low[u] = min(low[u], low[v])
                if not graph.directed and low[v] > d[u]:
                    bridges.append((u, v))
                if not graph.directed and not root and low[v] >= d[u]:
                    articulation.add(u)
            elif color[v] == 'gray':
                edges['back'].append((u, v))
                low[u] = min(low[u], d[v])
            else:
                if d[u] < d[v]:
                    edges['forward'].append((u, v))
                else:
                    edges['cross'].append((u, v))
        color[u] = 'black'
        time[0] += 1
        f[u] = time[0]
        order.append(u)
        if root and not graph.directed and children > 1:
            articulation.add(u)

    for u in range(n):
        if color[u] == 'white':
            visit(u, root=True)

    scc = []
    if graph.directed:
        # Kosaraju: run DFS on transpose using reverse finish order
        gt = Graph(n, directed=True)
        for u in range(n):
            for e in graph.neighbors(u):
                gt.add_edge(e.v, e.u, e.w)
        color2 = {u: 'white' for u in range(n)}
        comp = []

        def visit_t(u: int):
            color2[u] = 'gray'
            comp.append(u)
            for e in gt.neighbors(u):
                v = e.v
                if color2[v] == 'white':
                    visit_t(v)
            color2[u] = 'black'

        for u in reversed(order):
            if color2[u] == 'white':
                comp = []
                visit_t(u)
                scc.append(comp)

    return {
        'color': color,
        'd': d,
        'f': f,
        'parent': parent,
        'edges': edges,
        'scc': scc,
        'articulation': sorted(list(articulation)),
        'bridges': bridges,
    }


def bfs(graph: Graph, s: int, inf_value: int = 10**12):
    """Breadth-first search from source s.

    Returns:
        color, d, parent, order
    """
    n = graph.n
    color = {u: 'white' for u in range(n)}
    d = {u: inf_value for u in range(n)}
    parent = {u: None for u in range(n)}
    q = Queue()
    color[s] = 'gray'
    d[s] = 0
    q.enqueue(s)
    order = []
    while not q.is_empty():
        u = q.dequeue()
        order.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if color[v] == 'white':
                color[v] = 'gray'
                d[v] = d[u] + 1
                parent[v] = u
                q.enqueue(v)
        color[u] = 'black'
    return color, d, parent, order


