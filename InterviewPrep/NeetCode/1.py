# Use hashmap to keep difference from current and current's index


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locations, result = {}, []

        for i in range(len(nums)):
            if nums[i] in locations:
                result = [locations[nums[i]], i]
                break

            locations[target - nums[i]] = i

        return result
