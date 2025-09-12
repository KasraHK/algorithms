from data_structures.heap import MinHeap, MaxHeap
from data_structures.queue import Queue
from data_structures.fibonacci_heap import FibonacciHeap


def main():
    h = MinHeap()
    for x in [5, 3, 7, 1]:
        h.push(x)
    print("minheap pop order:", [h.pop() for _ in range(4)])

    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print("queue:", q.dequeue(), q.dequeue(), q.dequeue())

    fh = FibonacciHeap()
    n1 = fh.insert(10, "a")
    n2 = fh.insert(3, "b")
    fh.decrease_key(n1, 1)
    print("fib extract min:", fh.extract_min())


if __name__ == "__main__":
    main()


