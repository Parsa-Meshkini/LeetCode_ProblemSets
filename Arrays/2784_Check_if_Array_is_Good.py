class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1: return False
        new = list(range(1, n+1)) + [n]
        new.sort()
        nums.sort()
        return nums == new