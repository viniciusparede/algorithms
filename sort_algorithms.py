import time


def insert_sort(arr: list) -> tuple:
    execution_time = 0
    num_swaps = 0
    num_iterations = 0

    a = arr.copy()

    start_time = time.time()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            num_swaps += 1
            num_iterations += 1

        a[j + 1] = key
        num_iterations += 1

    end_time = time.time()

    execution_time = end_time - start_time

    return execution_time, num_swaps, num_iterations, a


def selection_sort(arr: list) -> tuple:
    execution_time = 0
    num_swaps = 0
    num_iterations = 0

    a = arr.copy()

    start_time = time.time()

    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            num_iterations += 1
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = (
                a[min_index],
                a[i],
            )
            num_swaps += 1

    end_time = time.time()

    execution_time = end_time - start_time

    return execution_time, num_swaps, num_iterations, a


def shell_sort(arr: list) -> tuple:
    execution_time = 0
    num_swaps = 0
    num_iterations = 0

    a = arr.copy()
    n = len(a)
    gap = n // 2

    start_time = time.time()
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            num_iterations += 1
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
                num_swaps += 1
            a[j] = temp
        gap //= 2

    end_time = time.time()

    execution_time = end_time - start_time

    return execution_time, num_swaps, num_iterations, a


def quick_sort(arr: list) -> tuple:
    def partition(a, low, high):
        pivot_index = (low + high) // 2
        pivot = a[pivot_index]

        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps[0] += 1

        i = low - 1
        for j in range(low, high):
            iterations[0] += 1
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps[0] += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps[0] += 1

        return i + 1

    def quick_sort_helper(a, low, high):
        if low < high:
            pivot_index = partition(a, low, high)
            quick_sort_helper(a, low, pivot_index - 1)
            quick_sort_helper(a, pivot_index + 1, high)

    swaps = [0]
    iterations = [0]
    a = arr.copy()

    start_time = time.time()
    quick_sort_helper(a, 0, len(a) - 1)
    end_time = time.time()

    execution_time = end_time - start_time

    return execution_time, swaps[0], iterations[0], a
