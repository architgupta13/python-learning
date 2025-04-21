from typing import List


def binary_search_non_recursive(arr: List[int], key: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr: List[int], low: int, high: int, key: int) -> int:
    if high < low:
        return -1

    mid = low + ((high - low) // 2)
    if arr[mid] == key:
        return mid

    if arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, high, key)

    return binary_search_recursive(arr, low, mid - 1, key)


arr = [1, 3, 4, 7, 8, 10]
print(binary_search_non_recursive(arr, 1))
print(binary_search_non_recursive(arr, 8))
print(binary_search_non_recursive(arr, 9))
print(binary_search_recursive(arr, 0, len(arr) - 1, 1))
print(binary_search_recursive(arr, 0, len(arr) - 1, 8))
print(binary_search_recursive(arr, 0, len(arr) - 1, 9))
