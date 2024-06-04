"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []



Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def __init__(self):
        self.results = set()

    def twoSum(self, nums: List[int], target: int) -> None:
        visited = dict()

        for idx, item in enumerate(nums):
            if target - item not in visited.keys():
                visited[item] = idx
            else:
                arr = sorted([target * (-1), item, target - item])
                self.results.add((arr[0], arr[1], arr[2]))

    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        targets = dict()

        for idx, item in enumerate(nums):
            targets[item] = idx

        for k, v in targets.items():
            arr = nums[0:v] + nums[v + 1 :] if v != len(nums) - 1 else nums[0:v]
            self.twoSum(arr, k * (-1))

        return [[x[0], x[1], x[2]] for x in list(self.results)]

    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = list()

        for idx, item in enumerate(nums):
            if idx != 0 and item == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                tmp_sum = nums[idx] + nums[left] + nums[right]
                if tmp_sum == 0:
                    results.append([nums[idx], nums[left], nums[right]])
                    # move left pointer forward to continue looping
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                elif tmp_sum > 0:
                    right = right - 1
                else:
                    left = left + 1

        return results
