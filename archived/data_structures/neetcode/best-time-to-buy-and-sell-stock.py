"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


"""

from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        max_rights = [0 for i in range(len(prices))]
        max_val = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i + 1] > max_val:
                max_val = prices[i + 1]
            max_rights[i] = max_val

        ans = 0
        for i in range(len(max_rights) - 1):
            if ans < max_rights[i] - prices[i]:
                ans = max_rights[i] - prices[i]

        return ans

    def maxProfit_2(self, prices: List[int]) -> int:
        ans = 0
        tmp_max = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            tmp_max = max(tmp_max, prices[i + 1])
            ans = max(ans, tmp_max - prices[i])

        return ans

    def maxProfit_3(self, prices: List[int]) -> int:
        ans = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                ans = max(ans, diff)
            else:
                left = right
            right += 1

        return ans
