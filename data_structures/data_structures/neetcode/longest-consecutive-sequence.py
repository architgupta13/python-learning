"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive_1(self, nums: List[int]) -> int:
        uniq = set(nums)
        result = 0

        for num in nums:
            if num - 1 in uniq:
                continue
            curr_max = 1
            i = 1
            while num + i in uniq:
                curr_max += 1
                i += 1

            max(result, curr_max)

        return result

    def longestConsecutive_2(self, nums: List[int]) -> int:
        uniq = set(nums)
        result = 0

        for num in nums:
            if num - 1 in uniq:
                continue
            length = 0
            while num + length in uniq:
                length += 1
            result = max(result, length)

        return result
