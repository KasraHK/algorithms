class TreeNode:
    """Binary tree node for trees and Huffman coding.

    Attributes:
        key: optional comparable identifier or weight
        value: payload value (e.g., symbol for Huffman)
        left: left child
        right: right child
        parent: parent node
    """

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __repr__(self):
        return f"TreeNode(key={self.key}, value={self.value})"


class GraphNode:
    """Graph node representation with id and optional data."""

    def __init__(self, node_id, data=None):
        self.id = node_id
        self.data = data

    def __repr__(self):
        return f"GraphNode(id={self.id})"


