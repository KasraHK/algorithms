def hanoi(i, j, n):
    if n == 1:
        print(f"Move disk from {i} to {j}")
        return 
    hanoi(i, 6 - i - j, n - 1)
    print(f"Move disk from {i} to {j}")
    hanoi(6 - i - j, j, n - 1)
    