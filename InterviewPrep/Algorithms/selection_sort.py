from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    start = 0
    while start < len(arr):
        min_idx, min_val = start, arr[start]
        for idx in range(start + 1, len(arr)):
            if arr[idx] < min_val:
                min_val = arr[idx]
                min_idx = idx

        if arr[start] > arr[min_idx]:
            arr[start], arr[min_idx] = arr[min_idx], arr[start]

        start += 1

    return arr


unsorted_arr = [5, 3, 2, 4, 1, 6]
print(selection_sort(unsorted_arr))

unsorted_arr = [1, 1, 1, 1, 1]
print(selection_sort(unsorted_arr))
