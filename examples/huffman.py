from algorithms.greedy.huffman import build_huffman_tree, huffman_codes


def main():
    symbols = [("a", 30), ("b", 10), ("c", 7), ("d", 8), ("e", 40), ("f", 14)]
    root = build_huffman_tree(symbols)
    codes = huffman_codes(root)
    print(codes)


if __name__ == "__main__":
    main()


