from typing import List


def linear_search(arr: List[int], key: int) -> int:
    for idx, val in enumerate(arr):
        if val == key:
            return idx

    return -1


arr = [5, 3, 2, 4, 1, 6]
print(linear_search(arr, 5))
print(linear_search(arr, 6))
print(linear_search(arr, 7))
