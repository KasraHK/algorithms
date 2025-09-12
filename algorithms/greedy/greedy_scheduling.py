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
    idx = list(range(n))
    idx.sort(key=lambda i: finishes.get(0, i))
    selected = []
    last_finish = -10**18
    for i in idx:
        if starts.get(0, i) >= last_finish:
            selected.append(i)
            last_finish = finishes.get(0, i)
    return selected


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
    idx = list(range(n))
    idx.sort(key=lambda i: profits.get(0, i), reverse=True)
    max_d = 0
    for i in range(n):
        d = deadlines.get(0, i)
        if d > max_d:
            max_d = d
    schedule = [-1] * max_d
    total = 0
    for i in idx:
        d = deadlines.get(0, i)
        # find latest free slot <= d
        t = min(d, max_d) - 1
        while t >= 0 and schedule[t] != -1:
            t -= 1
        if t >= 0:
            schedule[t] = i
            total += profits.get(0, i)
    return schedule, total


