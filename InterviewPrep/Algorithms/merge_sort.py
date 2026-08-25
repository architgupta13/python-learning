from typing import List


def merge(arr: List[int], start: int, mid: int, end: int) -> None:
    left = [arr[m] for m in range(start, mid + 1)]
    right = [arr[m] for m in range(mid + 1, end + 1)]

    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merging(arr: List[int], start: int, end: int) -> None:
    if start >= end:
        return

    mid = start + (end-start) // 2

    merging(arr, start, mid)
    merging(arr, mid+1, end)
    merge(arr, start, mid, end)

def merge_sort(arr: List[int]) -> List[int]:
    merging(arr, 0, len(arr)-1)
    return arr


unsorted_arr = [5, 3, 2, 4, 1, 6]
print(merge_sort(unsorted_arr))

unsorted_arr = [1, 1, 1, 1, 1]
print(merge_sort(unsorted_arr))

unsorted_arr = [5, 3, 2, 1, -54]
print(merge_sort(unsorted_arr))
