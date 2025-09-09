def merge(a, l, mid, r):
    left = a[l:mid + 1]
    right = a[mid + 1:r + 1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):  # a is the array, l the left index and r the right index)
    if l < r:
        mid = (l+r) // 2
        merge_sort(a, l, mid)  # Sort the left half
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)
        
        

import random
import time
arr = [random.randint(0, 100000000000) for _ in range(1000000)]
start = time.time()
#merge_sort(arr, 0, len(arr) - 1)
arr.sort()  # Using Python's built-in sort for comparison
end = time.time()
print(f"{end - start:.3f}")

