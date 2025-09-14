"""Queue data structure implemented with a circular buffer."""


from data_structures.matrix import Matrix


class QueueEmptyError(Exception):
    """Raised when dequeuing from an empty queue."""


class Queue:
    """A simple FIFO queue implemented with a circular buffer.

    Methods
    - enqueue(item): add to tail
    - dequeue(): remove from head
    - peek(): view head without removing
    - is_empty(): whether queue is empty
    - __len__(): current number of items
    """

    def __init__(self, capacity: int = 16):
        self._data = Matrix(1, max(1, capacity))
        self._head = 0
        self._tail = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _grow(self):
        new_capacity = max(2 * self._data.cols, 1)
        new_data = Matrix(1, new_capacity)
        for i in range(self._size):
            new_data.set(0, i, self._data.get(0, (self._head + i) % self._data.cols))
        self._data = new_data
        self._head = 0
        self._tail = self._size

    def enqueue(self, item) -> None:
        if self._size == self._data.cols:
            self._grow()
        self._data.set(0, self._tail, item)
        self._tail = (self._tail + 1) % self._data.cols
        self._size += 1

    def peek(self):
        if self._size == 0:
            raise QueueEmptyError("Queue is empty")
        return self._data.get(0, self._head)

    def dequeue(self):
        if self._size == 0:
            raise QueueEmptyError("Queue is empty")
        item = self._data.get(0, self._head)
        self._data.set(0, self._head, None)
        self._head = (self._head + 1) % self._data.cols
        self._size -= 1
        return item


