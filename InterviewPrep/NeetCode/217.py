# Check using set length

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqs = set(nums)
        return len(uniqs) != len(nums)
