class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if len(nums) < 2:
            return nums[0]
        while low < high:

            mid = (high + low) // 2

            if nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
