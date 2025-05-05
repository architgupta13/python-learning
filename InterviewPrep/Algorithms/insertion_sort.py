from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
	sorted_end = 0
	while sorted_end + 1 < len(arr):
		if arr[sorted_end] > arr[sorted_end + 1]:
			tmp, i = arr[sorted_end + 1], sorted_end

			while i > -1 and tmp < arr[i]:
				arr[i+1] = arr[i]
				i -= 1
			arr[i+1] = tmp

		sorted_end += 1
	return arr


unsorted_arr = [5, 3, 2, 4, 1, 6]
print(insertion_sort(unsorted_arr))

unsorted_arr = [1, 1, 0, 1, 1]
print(insertion_sort(unsorted_arr))

unsorted_arr = [5, 3, 2, 1, -54]
print(insertion_sort(unsorted_arr))