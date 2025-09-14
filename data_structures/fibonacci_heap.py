"""Fibonacci heap implementation.

Includes node class and heap with standard operations for demos.
"""


class FibNode:
    """Node for Fibonacci Heap.

    Attributes:
        key: comparable key for ordering
        value: associated payload
        degree: number of children
        mark: child cut mark
        parent, child, left, right: structural pointers (circular doubly linked list)
    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

    def __repr__(self):
        return f"FibNode(key={self.key}, degree={self.degree})"


class FibonacciHeap:
    """Fibonacci Heap with insert, merge, find_min, extract_min, decrease_key.

    Complexity (amortized):
      - insert, merge: O(1)
      - find_min: O(1)
      - extract_min: O(log n)
      - decrease_key: O(1)
    """

    def __init__(self):
        self.min = None
        self.n = 0

    def is_empty(self) -> bool:
        return self.min is None

    def insert(self, key, value=None) -> FibNode:
        """Insert and return the new node."""
        node = FibNode(key, value)
        self._merge_with_root_list(node)
        if self.min is None or node.key < self.min.key:
            self.min = node
        self.n += 1
        return node

    def minimum(self):
        """Return the minimum node or None."""
        return self.min

    def merge(self, other: 'FibonacciHeap') -> 'FibonacciHeap':
        """Meld two heaps and return self."""
        if other is None or other.min is None:
            return self
        if self.min is None:
            self.min = other.min
            self.n = other.n
            return self
        # concatenate root lists
        self._concatenate_root_lists(self.min, other.min)
        if other.min.key < self.min.key:
            self.min = other.min
        self.n += other.n
        return self

    def extract_min(self):
        """Remove and return the minimum node."""
        z = self.min
        if z is not None:
            # add children to root list
            if z.child is not None:
                children = []
                for x in self._iterate_list(z.child):
                    children.append(x)
                for x in children:
                    self._merge_with_root_list(x)
                    x.parent = None
            # remove z from root list
            self._remove_from_list(z)
            if z == z.right:  # was the only node
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.n -= 1
        return z

    def decrease_key(self, x: FibNode, k) -> None:
        """Decrease node x's key to k (k must be <= current key)."""
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if self.min is None or x.key < self.min.key:
            self.min = x

    # ---- Internal helpers ----
    def _merge_with_root_list(self, node: FibNode):
        if self.min is None:
            node.left = node.right = node
        else:
            # insert node into root list next to min
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node

    def _concatenate_root_lists(self, a: FibNode, b: FibNode):
        a_right = a.right
        b_left = b.left
        a.right = b
        b.left = a
        a_right.left = b_left
        b_left.right = a_right

    def _remove_from_list(self, x: FibNode):
        x.left.right = x.right
        x.right.left = x.left
        x.left = x.right = x

    def _iterate_list(self, start: FibNode):
        x = start
        while True:
            yield x
            x = x.right
            if x == start:
                break

    def _link(self, y: FibNode, x: FibNode):
        # remove y from root list and make it child of x
        self._remove_from_list(y)
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y.right = y
        else:
            # insert y into x's child list
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
        x.degree += 1
        y.mark = False

    def _consolidate(self):
        import math
        max_degree = int(math.log2(self.n)) + 2 if self.n > 0 else 1
        A = [None] * (max_degree + 1)
        roots = []
        if self.min:
            for w in self._iterate_list(self.min):
                roots.append(w)
        for w in roots:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if y.key < x.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None
        for a in A:
            if a is not None:
                if self.min is None:
                    self.min = a
                    a.left = a.right = a
                else:
                    self._merge_with_root_list(a)
                    if a.key < self.min.key:
                        self.min = a

    def _cut(self, x: FibNode, y: FibNode):
        # remove x from y's child list
        if y.child == x:
            if x.right != x:
                y.child = x.right
            else:
                y.child = None
        self._remove_from_list(x)
        y.degree -= 1
        self._merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y: FibNode):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)


