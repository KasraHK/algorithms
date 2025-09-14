from algorithms.greedy.huffman import build_huffman_tree, huffman_codes

def main():
    symbols = [("a", 1),("b", 1),("c", 2),("d", 3),("e", 5),("f", 8),("g", 13)]
    root = build_huffman_tree(symbols)
    codes = huffman_codes(root)
    print("Huffman Codes (fibonacci frequencies):", codes)


if __name__ == "__main__":
    main()


