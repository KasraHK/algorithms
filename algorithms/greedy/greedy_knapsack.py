from data_structures.matrix import Matrix


def fractional_knapsack(p: Matrix, w: Matrix, capacity: int):
    """Fractional knapsack using value/weight ratio.

    Args:
        p: 1xN Matrix of profits
        w: 1xN Matrix of weights
        capacity: maximum carry weight
    Returns:
        x: 1xN Matrix fractions selected (0..1)
        total_value: total profit achieved
    """
    if p.rows != 1 or w.rows != 1 or p.cols != w.cols:
        raise ValueError("p and w must be 1xN and same length")
    n = p.cols
    idx = list(range(n))
    # sort indices by ratio p/w descending
    idx.sort(key=lambda i: p.get(0, i) / w.get(0, i), reverse=True)
    x = Matrix(1, n, 0)
    remaining = capacity
    total_value = 0
    for i in idx:
        if remaining <= 0:
            break
        take = min(w.get(0, i), remaining)
        frac = take / w.get(0, i)
        x.set(0, i, frac)
        total_value += frac * p.get(0, i)
        remaining -= take
    return x, total_value


def linear_time_knapsack(p: Matrix, w: Matrix, capacity: int):
    """Expected linear-time fractional knapsack via selection/partitioning on value/weight ratio.

    This avoids a full sort by repeatedly partitioning items by ratio around a pivot.
    It returns the same optimal result as the sorting-based fractional knapsack.

    Args:
        p: 1xN Matrix of profits
        w: 1xN Matrix of weights
        capacity: carry capacity
    Returns:
        x: 1xN Matrix of fractions selected (0..1)
        total_value: total profit achieved
    """
    if p.rows != 1 or w.rows != 1 or p.cols != w.cols:
        raise ValueError("p and w must be 1xN and same length")
    n = p.cols

    def ratio(i: int) -> float:
        wi = w.get(0, i)
        return p.get(0, i) / wi if wi != 0 else float('inf')

    def solve(idx_list, rc, x_vec):
        if rc <= 0 or not idx_list:
            return 0.0
        if len(idx_list) == 1:
            i = idx_list[0]
            take = min(w.get(0, i), rc)
            frac = 0.0 if w.get(0, i) == 0 else take / w.get(0, i)
            x_vec.set(0, i, frac)
            return frac * p.get(0, i)

        pivot = idx_list[len(idx_list) // 2]
        r_piv = ratio(pivot)
        greater = []  # ratio > r_piv
        equal = []    # ratio == r_piv
        less = []     # ratio < r_piv
        for i in idx_list:
            r = ratio(i)
            if r > r_piv:
                greater.append(i)
            elif r < r_piv:
                less.append(i)
            else:
                equal.append(i)

        weight_greater = sum(w.get(0, i) for i in greater)
        if weight_greater > rc:
            # All optimal mass lives in greater set
            return solve(greater, rc, x_vec)

        total = 0.0
        # Take all greater fully
        for i in greater:
            x_vec.set(0, i, 1.0)
            total += p.get(0, i)
        rc2 = rc - weight_greater

        weight_equal = sum(w.get(0, i) for i in equal)
        if weight_equal <= rc2:
            # Take all equals fully and continue in less
            for i in equal:
                x_vec.set(0, i, 1.0)
                total += p.get(0, i)
            rc3 = rc2 - weight_equal
            return total + solve(less, rc3, x_vec)
        else:
            # Capacity is within the equal-ratio set; fill fractionally
            remaining = rc2
            for i in equal:
                if remaining <= 0:
                    break
                wi = w.get(0, i)
                take = min(wi, remaining)
                frac = 0.0 if wi == 0 else take / wi
                x_vec.set(0, i, frac)
                total += frac * p.get(0, i)
                remaining -= take
            return total

    x = Matrix(1, n, 0)
    total_value = solve(list(range(n)), capacity, x)
    return x, total_value


