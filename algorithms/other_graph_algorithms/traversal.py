from data_structures.graph import Graph
from data_structures.queue import Queue
from data_structures.matrix import Matrix


def dfs(graph: Graph):
    """Depth-first search with discovery/finish times and parents.

    Supports arbitrary vertex ids by using dicts keyed by vertex id.

    Args:
        graph: Graph instance (directed or undirected)

    Returns:
        color: dict vertex -> 'white'|'gray'|'black' state
        d: dict vertex -> discovery time
        f: dict vertex -> finish time
        parent: dict vertex -> predecessor in DFS forest
    """
    color = {u: 'white' for u in graph.adj.keys()}
    d = {u: 0 for u in graph.adj.keys()}
    f = {u: 0 for u in graph.adj.keys()}
    parent = {u: None for u in graph.adj.keys()}
    time = [0]

    def visit(u):
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

    for u in list(graph.adj.keys()):
        if color[u] == 'white':
            visit(u)
    return color, d, f, parent


def dfs_plus(graph: Graph):
    """DFS with edge classification, SCC (for directed), articulation points, and bridges.

    Supports arbitrary vertex ids by using dicts keyed by vertex id. For SCC,
    runs Kosaraju on a dynamically built transpose graph.

    Args:
        graph: Graph instance

    Returns:
        dict with keys:
          - color: vertex -> color
          - d: vertex -> discovery time
          - f: vertex -> finish time
          - parent: vertex -> predecessor
          - edges: dict with lists for 'tree', 'back', 'forward', 'cross'
          - scc: list of strongly connected components (lists of vertices)
          - articulation: list of articulation points (undirected only)
          - bridges: list of (u, v) bridge edges (undirected only)
    """
    color = {u: 'white' for u in graph.adj.keys()}
    d = {u: 0 for u in graph.adj.keys()}
    f = {u: 0 for u in graph.adj.keys()}
    parent = {u: None for u in graph.adj.keys()}
    time = [0]
    edges = { 'tree': Matrix(0, 2), 'back': Matrix(0, 2), 'forward': Matrix(0, 2), 'cross': Matrix(0, 2) }
    low = {u: 0 for u in graph.adj.keys()}
    articulation_set = set()
    bridges_matrix = Matrix(0, 2)

    order = []

    def visit(u, root=False):
        color[u] = 'gray'
        time[0] += 1
        d[u] = low[u] = time[0]
        children = 0
        for e in graph.neighbors(u):
            v = e.v
            if color[v] == 'white':
                edges['tree'].add_row([u, v])
                parent[v] = u
                children += 1
                visit(v)
                low[u] = min(low[u], low[v])
                if not graph.directed and low[v] > d[u]:
                    bridges_matrix.add_row([u, v])
                if not graph.directed and not root and low[v] >= d[u]:
                    articulation_set.add(u)
            elif color[v] == 'gray':
                edges['back'].add_row([u, v])
                low[u] = min(low[u], d[v])
            else:
                if d[u] < d[v]:
                    edges['forward'].add_row([u, v])
                else:
                    edges['cross'].add_row([u, v])
        color[u] = 'black'
        time[0] += 1
        f[u] = time[0]
        order.append(u)
        if root and not graph.directed and children > 1:
            articulation_set.add(u)

    for u in list(graph.adj.keys()):
        if color[u] == 'white':
            visit(u, root=True)

    scc_matrices = []
    if graph.directed:
        # Kosaraju: run DFS on transpose using reverse finish order
        gt = Graph(0, directed=True)
        for u in graph.adj.keys():
            for e in graph.neighbors(u):
                gt.add_edge(e.v, e.u, e.w)
        color2 = {u: 'white' for u in gt.adj.keys()}
        
        def visit_t(u, current_comp_list):
            color2[u] = 'gray'
            current_comp_list.append(u)
            for e in gt.neighbors(u):
                v = e.v
                if color2[v] == 'white':
                    visit_t(v, current_comp_list)
            color2[u] = 'black'

        for u in reversed(order):
            if color2[u] == 'white':
                comp_list = []
                visit_t(u, comp_list)
                comp_matrix = Matrix(1, len(comp_list))
                for i, vertex in enumerate(comp_list):
                    comp_matrix.set(0, i, vertex)
                scc_matrices.append(comp_matrix)
    
    articulation_list = sorted(list(articulation_set))
    articulation_matrix = Matrix(1, len(articulation_list))
    for i, vertex in enumerate(articulation_list):
        articulation_matrix.set(0, i, vertex)

    return {
        'color': color,
        'd': d,
        'f': f,
        'parent': parent,
        'edges': edges,
        'scc': scc_matrices,
        'articulation': articulation_matrix,
        'bridges': bridges_matrix,
    }


def bfs(graph: Graph, s, inf_value: int = 10**12):
    """Breadth-first search from source s.

    Supports arbitrary vertex ids by using dicts keyed by vertex id.

    Args:
        graph: Graph instance
        s: source vertex id
        inf_value: distance for unreachable vertices

    Returns:
        color: dict vertex -> 'white'|'gray'|'black'
        d: dict vertex -> BFS distance from s
        parent: dict vertex -> predecessor
        order: Matrix of vertices in dequeue order
    """
    color = {u: 'white' for u in graph.adj.keys()}
    d = {u: inf_value for u in graph.adj.keys()}
    parent = {u: None for u in graph.adj.keys()}
    q = Queue()
    color[s] = 'gray'
    d[s] = 0
    q.enqueue(s)
    order_list = []
    while not q.is_empty():
        u = q.dequeue()
        order_list.append(u)
        for e in graph.neighbors(u):
            v = e.v
            if color.get(v) == 'white':
                color[v] = 'gray'
                d[v] = d[u] + 1
                parent[v] = u
                q.enqueue(v)
        color[u] = 'black'

    order_matrix = Matrix(1, len(order_list))
    for i, vertex in enumerate(order_list):
        order_matrix.set(0, i, vertex)
        
    return color, d, parent, order_matrix


