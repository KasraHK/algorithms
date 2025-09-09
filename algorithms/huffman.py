class node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Value: {self.value}, Freq: {self.freq}, Left: <{self.left}>, Right: <{self.right}>"
    
    def recursive_code(self, current_code=""):
        if self.value is not None:
            print(f"{self.value}: {current_code}")
        if self.left:
            self.left.recursive_code(current_code + "0")
        if self.right:
            self.right.recursive_code(current_code + "1")
        


def heapify(arr: list[node]):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        if arr[i].freq > arr[2 * i + 1].freq and 2 * i + 1 < n:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
        if 2 * i + 2 < n and arr[i].freq > arr[2 * i + 2].freq:
            arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]

        
def huffman(heap):
    while len(heap) > 1:
        left = heap.pop(0)
        heapify(heap)
        right = heap.pop(0)
        newNode = node(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right
        heap.append(newNode)
        heapify(heap)
    

initial_array = [node("a", 30), node("b", 10), node("c", 7), node("D", 8), node("e", 40), node("f", 14)]

heap = initial_array[:]
heapify(heap)
huffman(heap)
heap[0].recursive_code()
print(heap)
