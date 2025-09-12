from data_structures.matrix import Matrix
from algorithms.greedy_knapsack import fractional_knapsack, linear_time_knapsack
from algorithms.greedy_scheduling import activity_selection, deadline_scheduler


def main():
    p = Matrix(1, 4)
    w = Matrix(1, 4)
    for i, val in enumerate([60, 100, 120, 80]):
        p.set(0, i, val)
    for i, val in enumerate([10, 20, 30, 40]):
        w.set(0, i, val)
    x, val = fractional_knapsack(p, w, 50)
    print("fractional value:", val)

    x01, val01 = linear_time_knapsack(p, w, 50)
    print("0/1 knapsack value:", val01)

    s = Matrix(1, 5)
    f = Matrix(1, 5)
    for i, val in enumerate([1, 3, 0, 5, 8]):
        s.set(0, i, val)
    for i, val in enumerate([2, 4, 6, 7, 9]):
        f.set(0, i, val)
    print("activities:", activity_selection(s, f))

    d = Matrix(1, 5)
    prof = Matrix(1, 5)
    for i, val in enumerate([2, 1, 2, 1, 3]):
        d.set(0, i, val)
    for i, val in enumerate([100, 19, 27, 25, 15]):
        prof.set(0, i, val)
    sched, tot = deadline_scheduler(d, prof)
    print("deadline total:", tot, "schedule:", sched)


if __name__ == "__main__":
    main()


