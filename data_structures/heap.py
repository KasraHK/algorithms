"""Binary heap implementations: MinHeap and MaxHeap."""


from data_structures.matrix import Matrix


class HeapEmptyError(Exception):
    """Raised when extracting from an empty heap."""


class MinHeap:
    """A binary min-heap.

    Supports push, peek, pop, size, and is_empty operations.
    Stores arbitrary comparable items; for keyed items use tuples (key, value).
    """

    def __init__(self):
        self._data = Matrix(1, 0)

    def __len__(self):
        return self._data.cols

    def is_empty(self) -> bool:
        return self._data.cols == 0

    def push(self, item):
        """Insert item into heap.

        Args:
            item: comparable object
        Returns: None
        """
        self._data.add_column([item])
        self._sift_up(self._data.cols - 1)

    def peek(self):
        """Return min item without removing it.

        Raises HeapEmptyError if empty.
        """
        if self.is_empty():
            raise HeapEmptyError("Heap is empty")
        return self._data.get(0, 0)

    def pop(self):
        """Remove and return min item.

        Raises HeapEmptyError if empty.
        """
        if self.is_empty():
            raise HeapEmptyError("Heap is empty")
        last_idx = self._data.cols - 1
        self._swap(0, last_idx)
        item = self._data.get(0, last_idx)
        self._data.cols -= 1
        new_data = Matrix(1, self._data.cols)
        for i in range(self._data.cols):
            new_data.set(0, i, self._data.get(0, i))
        self._data = new_data
        if not self.is_empty():
            self._sift_down(0)
        return item

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        self._data.swap(i, j)

    def _sift_up(self, i: int):
        while i > 0:
            p = self._parent(i)
            if self._data.get(0, i) < self._data.get(0, p):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int):
        n = self._data.cols
        while True:
            l, r = self._left(i), self._right(i)
            smallest = i
            if l < n and self._data.get(0, l) < self._data.get(0, smallest):
                smallest = l
            if r < n and self._data.get(0, r) < self._data.get(0, smallest):
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
            if self._data.get(0, i) > self._data.get(0, p):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int):
        n = self._data.cols
        while True:
            l, r = self._left(i), self._right(i)
            largest = i
            if l < n and self._data.get(0, l) > self._data.get(0, largest):
                largest = l
            if r < n and self._data.get(0, r) > self._data.get(0, largest):
                largest = r
            if largest == i:
                break
            self._swap(i, largest)
            i = largest


