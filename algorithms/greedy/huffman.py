from data_structures.heap import MinHeap
from data_structures.nodes import TreeNode


def build_huffman_tree(symbols_with_freq):
    """Build Huffman tree using MinHeap of (frequency, counter, TreeNode).

    Args:
        symbols_with_freq: iterable of (symbol, frequency)
    Returns:
        root TreeNode of the Huffman tree
    """
    heap = MinHeap()
    counter = 0
    for sym, freq in symbols_with_freq:
        node = TreeNode(key=freq, value=sym)
        heap.push((freq, counter, node))
        counter += 1

    while len(heap) > 1:
        f1, _, n1 = heap.pop()
        f2, _, n2 = heap.pop()
        parent = TreeNode(key=f1 + f2, value=None)
        parent.left = n1
        parent.right = n2
        n1.parent = parent
        n2.parent = parent
        heap.push((parent.key, counter, parent))
        counter += 1
    return heap.pop()[2]


def huffman_codes(root: TreeNode):
    """Generate Huffman codes from the tree root.

    Returns:
        dict mapping symbol to bitstring code
    """
    codes = {}

    def dfs(node: TreeNode, prefix: str):
        if node is None:
            return
        if node.is_leaf() and node.value is not None:
            codes[node.value] = prefix or "0"
            return
        dfs(node.left, prefix + "0")
        dfs(node.right, prefix + "1")

    dfs(root, "")
    return codes


if __name__ == "__main__":
    initial = [("a", 30), ("b", 10), ("c", 7), ("D", 8), ("e", 40), ("f", 14)]
    root = build_huffman_tree(initial)
    codes = huffman_codes(root)
    print(codes)
