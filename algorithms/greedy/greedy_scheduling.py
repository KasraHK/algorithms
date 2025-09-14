from data_structures.matrix import Matrix


def activity_selection(starts: Matrix, finishes: Matrix):
    """Select maximum number of non-overlapping activities.

    Args:
        starts: 1xN Matrix of start times
        finishes: 1xN Matrix of finish times
    Returns:
        selected_indices: list of selected activity indices in order
    """
    if starts.rows != 1 or finishes.rows != 1 or starts.cols != finishes.cols:
        raise ValueError("starts and finishes must be 1xN and same length")
    n = starts.cols
    idx_matrix = Matrix(1, n)
    for i in range(n):
        idx_matrix.set(0, i, i)

    # Sorting logic similar to knapsack
    idx_list = [idx_matrix.get(0, i) for i in range(n)]
    idx_list.sort(key=lambda i: finishes.get(0, i))
    for i in range(n):
        idx_matrix.set(0, i, idx_list[i])

    selected_matrix = Matrix(1, 0)
    last_finish = -10**18
    for i in range(n):
        activity_idx = idx_matrix.get(0, i)
        if starts.get(0, activity_idx) >= last_finish:
            selected_matrix.add_column([activity_idx])
            last_finish = finishes.get(0, activity_idx)
    return selected_matrix


def deadline_scheduler(deadlines: Matrix, profits: Matrix):
    """Job sequencing with deadlines (unit time jobs).

    Args:
        deadlines: 1xN Matrix of deadlines (positive integers)
        profits: 1xN Matrix of profits
    Returns:
        schedule: list of job indices placed in slots (length = max_deadline), -1 for empty
        total_profit: sum of profits of scheduled jobs
    """
    if deadlines.rows != 1 or profits.rows != 1 or deadlines.cols != profits.cols:
        raise ValueError("deadlines and profits must be 1xN and same length")
    n = deadlines.cols
    idx_matrix = Matrix(1, n)
    for i in range(n):
        idx_matrix.set(0, i, i)
    
    idx_list = [idx_matrix.get(0, i) for i in range(n)]
    idx_list.sort(key=lambda i: profits.get(0, i), reverse=True)
    for i in range(n):
        idx_matrix.set(0, i, idx_list[i])

    max_d = 0
    for i in range(n):
        d = deadlines.get(0, i)
        if d > max_d:
            max_d = d
    
    schedule_matrix = Matrix(1, max_d, -1)
    total = 0
    for i in range(n):
        job_idx = idx_list[i]
        d = deadlines.get(0, job_idx)
        # find latest free slot <= d
        t = min(d, max_d) - 1
        while t >= 0 and schedule_matrix.get(0, t) != -1:
            t -= 1
        if t >= 0:
            schedule_matrix.set(0, t, job_idx)
            total += profits.get(0, job_idx)
    return schedule_matrix, total


