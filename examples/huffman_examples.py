from algorithms.greedy.huffman import build_huffman_tree, huffman_codes

def huffman_examples():
    print("--- Huffman Coding Examples ---")

    # Normal case: A sample text
    print("\n--- Normal Case: Sample Text ---")
    text = "this is an example of a huffman tree"
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    symbols = list(freq.items())
    print("Symbols and frequencies:", symbols)
    root = build_huffman_tree(symbols)
    codes = huffman_codes(root)
    print("Huffman Codes:", codes)
    encoded_text = "".join(codes[char] for char in text)
    print("Encoded text length:", len(encoded_text))

    # Edge case: Only one symbol
    print("\n--- Edge Case: Single Symbol ---")
    symbols_single = [('a', 10)]
    print("Symbols and frequencies:", symbols_single)
    root_single = build_huffman_tree(symbols_single)
    codes_single = huffman_codes(root_single)
    print("Huffman Codes:", codes_single)

    # Edge case: All symbols have the same frequency
    print("\n--- Edge Case: Uniform Frequencies ---")
    symbols_uniform = [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)]
    print("Symbols and frequencies:", symbols_uniform)
    root_uniform = build_huffman_tree(symbols_uniform)
    codes_uniform = huffman_codes(root_uniform)
    print("Huffman Codes:", codes_uniform)

if __name__ == "__main__":
    huffman_examples()
