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
    """Linear-time selection-based 0/1 knapsack assuming unit profits tie handling by partitioning.

    Partitions items by weight around a pivot repeatedly. Returns set membership x.
    This implements the described 3-way partition strategy over weights while prioritizing higher weights until capacity is filled.

    Args:
        p: 1xN Matrix of profits
        w: 1xN Matrix of weights
        capacity: carry capacity
    Returns:
        x: 1xN Matrix of 0/1 selections
    """
    if p.rows != 1 or w.rows != 1 or p.cols != w.cols:
        raise ValueError("p and w must be 1xN and same length")
    n = p.cols
    indices = Matrix(1, n)
    for i in range(n):
        indices.set(0, i, i)

    def solve(idx_list, rc):
        if rc <= 0 or not idx_list:
            return []
        if len(idx_list) == 1:
            i = idx_list[0]
            return [i] if w.get(0, i) <= rc else []
        pivot = idx_list[len(idx_list) // 2]
        wg = []
        we = []
        wl = []
        for i in idx_list:
            if w.get(0, i) > w.get(0, pivot):
                wg.append(i)
            elif w.get(0, i) == w.get(0, pivot):
                we.append(i)
            else:
                wl.append(i)
        sum_wg = sum(w.get(0, i) for i in wg)
        if sum_wg > rc:
            return solve(wg, rc)
        selected = list(wg)
        rc2 = rc - sum_wg
        # take as many equals as fit
        we.sort(key=lambda i: p.get(0, i), reverse=True)
        for i in we:
            if w.get(0, i) <= rc2:
                selected.append(i)
                rc2 -= w.get(0, i)
        if rc2 == 0:
            return selected
        return selected + solve(wl, rc2)

    chosen = solve(list(range(n)), capacity)
    x = Matrix(1, n, 0)
    for i in chosen:
        x.set(0, i, 1)
    total_value = sum(p.get(0, i) for i in chosen)
    return x, total_value


