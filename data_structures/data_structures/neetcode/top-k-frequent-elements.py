"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]



Constraints:

    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq_dict: dict = collections.defaultdict(int)

        for item in nums:
            uniq_dict[item] += 1

        counts: list = [[] for i in range(len(nums) + 1)]

        for key, val in uniq_dict.items():
            counts[val].append(key)

        results: list = []

        for item in reversed(counts):
            results.extend(item)

        return results[:k]
