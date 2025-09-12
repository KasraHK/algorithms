from data_structures.matrix import Matrix
from data_structures.queue import Queue, QueueEmptyError
from algorithms.quick_sort import quick_sort_matrix
from algorithms.two_pointers.partition import kth_smallest, sel
from algorithms.recursion.binary_search import binary_search, recursive_binary_search
from data_structures.graph import Graph
from algorithms.other_graph_algorithms.shortest_paths import dijkstra, bellman_ford
from algorithms.greedy.mst import prim_mst


def print_header(title):
    print("\n==", title, "==")


def test_matrix_sort_edge_cases():
    print_header("Matrix quick_sort edge cases")
    # empty vector
    v0 = Matrix(1, 0)
    quick_sort_matrix(v0)
    print("empty:", v0.len())  # Expected: 0
    # single element
    v1 = Matrix(1, 1); v1.set(0, 0, 42)
    quick_sort_matrix(v1)
    print("single:", v1.get(0, 0))  # Expected: 42
    # duplicates
    v = Matrix(1, 8)
    for i, x in enumerate([5, 2, 9, 1, 5, 6, 3, 7]):
        v.set(0, i, x)
    quick_sort_matrix(v)
    print([v.get(0, i) for i in range(v.cols)])  # Expected: [1,2,3,5,5,6,7,9]


def test_selection_edge_cases():
    print_header("kth_smallest / sel edge cases")
    arr = [3, 2, 1, 5, 4]
    m = Matrix(1, len(arr))
    for i, x in enumerate(arr):
        m.set(0, i, x)
    print("k=1:", kth_smallest(m, 1))  # Expected: 1
    print("k=5:", kth_smallest(m, 5))  # Expected: 5
    # median-of-medians deterministic select
    m2 = Matrix(1, len(arr))
    for i, x in enumerate(arr):
        m2.set(0, i, x)
    print("sel k=3:", sel(m2, 0, m2.len() - 1, 3))  # Expected: 3


def test_binary_search_edge_cases():
    print_header("Binary search edge cases")
    v = Matrix(1, 6)
    for i, val in enumerate([1, 3, 5, 7, 9, 11]):
        v.set(0, i, val)
    print("present 7:", binary_search(v, 7))  # Expected: True
    print("absent 8:", recursive_binary_search(v, 0, v.cols - 1, 8))  # Expected: False


def test_queue_edge_cases():
    print_header("Queue edge cases")
    q = Queue(1)
    q.enqueue(10)
    q.enqueue(20)  # triggers grow
    print("peek:", q.peek())  # Expected: 10
    print("dequeue:", q.dequeue(), q.dequeue())  # Expected: 10 20
    try:
        q.dequeue()
    except QueueEmptyError:
        print("dequeue on empty raises")  # Expected: prints this line


def test_graph_dijkstra_strings_unreachable():
    print_header("Dijkstra strings + unreachable")
    g = Graph(0, directed=False)
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    # 'Z' is unreachable
    order, d, parent = dijkstra(g, 'A')
    print("order:", order)  # Expected starts with 'A'
    print("dist C:", d.get('C'))  # Expected: 3
    print("dist Z:", d.get('Z'))  # Expected: None or inf sentinel not present


def test_bellman_ford_negative_cycle_strings():
    print_header("Bellman-Ford strings negative cycle")
    g = Graph(0, directed=True)
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 1)
    g.add_edge('C', 'A', -3)
    ok, d, parent = bellman_ford(g, 'A')
    print("ok:", ok)  # Expected: False


def test_prim_strings_total():
    print_header("Prim MST strings total")
    g = Graph(0, directed=False)
    g.add_edge('A', 'B', 2)
    g.add_edge('B', 'C', 3)
    g.add_edge('A', 'C', 4)
    parent, key, order, edges, total = prim_mst(g, start='A')
    print("total:", total)  # Expected: 5
    print("edges:", sorted(edges))  # Expected pairs covering all vertices


if __name__ == "__main__":
    test_matrix_sort_edge_cases()
    test_selection_edge_cases()
    test_binary_search_edge_cases()
    test_queue_edge_cases()
    test_graph_dijkstra_strings_unreachable()
    test_bellman_ford_negative_cycle_strings()
    test_prim_strings_total()