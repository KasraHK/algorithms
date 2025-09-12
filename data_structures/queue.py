class QueueEmptyError(Exception):
    """Raised when dequeuing from an empty queue."""


class Queue:
    """A simple FIFO queue implemented with a circular buffer.

    Provides enqueue, dequeue, peek, is_empty, and size operations.
    """

    def __init__(self, capacity: int = 16):
        self._data = [None] * max(1, capacity)
        self._head = 0
        self._tail = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _grow(self):
        new_capacity = max(2 * len(self._data), 1)
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % len(self._data)]
        self._data = new_data
        self._head = 0
        self._tail = self._size

    def enqueue(self, item) -> None:
        if self._size == len(self._data):
            self._grow()
        self._data[self._tail] = item
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def peek(self):
        if self._size == 0:
            raise QueueEmptyError("Queue is empty")
        return self._data[self._head]

    def dequeue(self):
        if self._size == 0:
            raise QueueEmptyError("Queue is empty")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return item


