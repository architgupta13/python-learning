"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105


"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # max water trapped at above a block is min(left boundary, right boundary) - height of block
        volume, left, right = 0, 0, len(height) - 1
        max_left, max_right = 0, 0

        while left < right:
            if height[left] <= height[right]:
                if left != 0 and max_left > height[left]:
                    volume += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if right != len(height) - 1 and max_right > height[right]:
                    volume += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1

        return volume
