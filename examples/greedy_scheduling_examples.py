from algorithms.greedy.greedy_scheduling import activity_selection, deadline_scheduler
from data_structures.matrix import Matrix

def greedy_scheduling_examples():
    print("--- Greedy Scheduling Examples ---")

    # Activity Selection - Normal Case
    print("\n--- Activity Selection: Normal Case ---")
    starts = Matrix(1, 11)
    starts.data[0] = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finishes = Matrix(1, 11)
    finishes.data[0] = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print("Start times:", starts)
    print("Finish times:", finishes)
    selected_activities = activity_selection(starts, finishes)
    print("Selected activities (indices):", selected_activities)

    # Activity Selection - Edge Case: No activities can be selected together
    print("\n--- Activity Selection: Edge Case - No Overlap Possible ---")
    starts_no = Matrix(1, 3)
    starts_no.data[0] = [1, 2, 3]
    finishes_no = Matrix(1, 3)
    finishes_no.data[0] = [5, 6, 7]
    print("Start times:", starts_no)
    print("Finish times:", finishes_no)
    selected_no = activity_selection(starts_no, finishes_no)
    print("Selected activities (indices):", selected_no)

    # Deadline Scheduler - Normal Case
    print("\n--- Deadline Scheduler: Normal Case ---")
    profits = Matrix(1, 7)
    profits.data[0] = [35, 30, 25, 20, 15, 12, 5]
    deadlines = Matrix(1, 7)
    deadlines.data[0] = [3, 4, 4, 2, 3, 1, 2]
    print("Profits:", profits)
    print("Deadlines:", deadlines)
    schedule, total_profit = deadline_scheduler(deadlines, profits)
    print("Schedule (job indices):", schedule)
    print("Total profit:", total_profit)

    # Deadline Scheduler - Edge Case: All jobs have deadline 1
    print("\n--- Deadline Scheduler: Edge Case - All Deadline 1 ---")
    profits_d1 = Matrix(1, 4)
    profits_d1.data[0] = [100, 10, 15, 27]
    deadlines_d1 = Matrix(1, 4)
    deadlines_d1.data[0] = [1, 1, 1, 1]
    print("Profits:", profits_d1)
    print("Deadlines:", deadlines_d1)
    schedule_d1, total_profit_d1 = deadline_scheduler(deadlines_d1, profits_d1)
    print("Schedule (job indices):", schedule_d1)
    print("Total profit:", total_profit_d1)

if __name__ == "__main__":
    greedy_scheduling_examples()
