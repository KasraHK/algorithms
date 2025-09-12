class HeapEmptyError(Exception):
    """Raised when extracting from an empty heap."""


class MinHeap:
    """A simple binary min-heap implemented without external libraries.

    Supports push, peek, pop, size, and is_empty operations.
    Stores arbitrary comparable items; for keyed items use tuples (key, value).
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, item):
        """Insert item into heap.

        Args:
            item: comparable object
        Returns: None
        """
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def peek(self):
        """Return min item without removing it.

        Raises HeapEmptyError if empty.
        """
        if not self._data:
            raise HeapEmptyError("Heap is empty")
        return self._data[0]

    def pop(self):
        """Remove and return min item.

        Raises HeapEmptyError if empty.
        """
        if not self._data:
            raise HeapEmptyError("Heap is empty")
        last_idx = len(self._data) - 1
        self._swap(0, last_idx)
        item = self._data.pop()
        if self._data:
            self._sift_down(0)
        return item

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i: int):
        while i > 0:
            p = self._parent(i)
            if self._data[i] < self._data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int):
        n = len(self._data)
        while True:
            l, r = self._left(i), self._right(i)
            smallest = i
            if l < n and self._data[l] < self._data[smallest]:
                smallest = l
            if r < n and self._data[r] < self._data[smallest]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest


class MaxHeap(MinHeap):
    """Binary max-heap by inverting comparison of MinHeap."""

    def _sift_up(self, i: int):
        while i > 0:
            p = self._parent(i)
            if self._data[i] > self._data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int):
        n = len(self._data)
        while True:
            l, r = self._left(i), self._right(i)
            largest = i
            if l < n and self._data[l] > self._data[largest]:
                largest = l
            if r < n and self._data[r] > self._data[largest]:
                largest = r
            if largest == i:
                break
            self._swap(i, largest)
            i = largest


