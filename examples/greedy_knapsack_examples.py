from algorithms.greedy.greedy_knapsack import fractional_knapsack
from data_structures.matrix import Matrix

def greedy_knapsack_examples():
    print("--- Greedy Knapsack Examples ---")

    # Normal case
    print("\n--- Normal Case ---")
    profits = Matrix(1, 5)
    profits.data[0] = [60, 100, 120, 80, 90]
    weights = Matrix(1, 5)
    weights.data[0] = [10, 20, 30, 15, 25]
    capacity = 50
    print("Profits:", profits)
    print("Weights:", weights)
    print("Capacity:", capacity)
    fractions, total_value = fractional_knapsack(profits, weights, capacity)
    print("Fractions taken:", fractions)
    print("Total value:", total_value)

    # Edge case: An item's weight is greater than capacity
    print("\n--- Edge Case: Item larger than capacity ---")
    profits_large = Matrix(1, 3)
    profits_large.data[0] = [60, 100, 120]
    weights_large = Matrix(1, 3)
    weights_large.data[0] = [10, 20, 60]
    capacity_small = 25
    print("Profits:", profits_large)
    print("Weights:", weights_large)
    print("Capacity:", capacity_small)
    fractions_large, total_value_large = fractional_knapsack(profits_large, weights_large, capacity_small)
    print("Fractions taken:", fractions_large)
    print("Total value:", total_value_large)

if __name__ == "__main__":
    greedy_knapsack_examples()
