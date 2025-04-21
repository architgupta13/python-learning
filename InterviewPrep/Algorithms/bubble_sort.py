from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    swaps_remaining = True

    while swaps_remaining:
        swaps_remaining = False
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps_remaining = True

    return arr


def bubble_sort_reduce_limit(arr: List[int]) -> List[int]:
    swaps_remaining, length = True, len(arr)

    while swaps_remaining:
        swaps_remaining = False
        for idx in range(length - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps_remaining = True
        length -= 1

    return arr


def bubble_sort_update_limit(arr: List[int]) -> List[int]:
    swaps_remaining, length = True, len(arr)

    while swaps_remaining:
        swaps_remaining = False
        for idx in range(length - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                length = idx + 1
                swaps_remaining = True

    return arr


unsorted_arr = [5, 3, 2, 4, 1, 6]
print(bubble_sort(unsorted_arr))

unsorted_arr = [5, 3, 2, 4, 1, 6]
print(bubble_sort_reduce_limit(unsorted_arr))

unsorted_arr = [5, 3, 2, 4, 1, 6]
print(bubble_sort_update_limit(unsorted_arr))
