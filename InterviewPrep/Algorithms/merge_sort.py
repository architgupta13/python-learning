from typing import List


def merge(arr: List[int], start: int, mid: int, end: int) -> None:
	lmax, rmax, i, j, res = mid-start+1, end-mid, start, mid+1, []

	while i < lmax and j < rmax:
		if arr[i] < arr[j]:
			res.append(arr[i])
			i += 1
		else:
			res.append(arr[j])
			j += 1

	if i < lmax:
		for k in range(i, lmax):
			res.append(arr[k])
	if j < rmax:
		for k in range(j, rmax):
			res.append(arr[k])


def merging(arr: List[int], start: int, end: int) -> None:
	if start >= end:
		return

	mid = start + (end-start) // 2

	merging(arr, start, mid)
	merging(arr, mid+1, end)
	merge(arr, start, mid, end)

def merge_sort(arr: List[int]) -> List[int]:
	merging(arr, 0, len(arr))
	return arr


unsorted_arr = [5, 3, 2, 4, 1, 6]
print(merge_sort(unsorted_arr))

unsorted_arr = [1, 1, 1, 1, 1]
print(merge_sort(unsorted_arr))

unsorted_arr = [5, 3, 2, 1, -54]
print(merge_sort(unsorted_arr))
