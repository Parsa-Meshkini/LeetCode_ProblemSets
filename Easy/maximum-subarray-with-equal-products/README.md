# 3411. Maximum Subarray With Equal Products

**Difficulty:** Easy
**Date:** 3411

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products)

## Solution Approach

The key insight is to use the logarithm of elements to convert product comparisons into sum comparisons, enabling the problem to reduce to finding the longest subarray with equal sum of logs. By storing prefix sums of logs and tracking indices of identical sums, we efficiently identify subarrays with equal products in O(n) time. This approach leverages prefix sums and hashing to avoid costly product computations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from math import gcd
# Approach: Two-pointer technique for optimal solution

# Trick: Process from end to beginning to avoid shifts
# Initialize with boundary case

from functools import reduce

class Solution:
    def maxProductEquivalentSubarray(self, nums: list[int]) -> int:
        # Helper to compute gcd of a list
        def gcd_list(items):
            return reduce(gcd, items)
        
        # Helper to compute lcm of two numbers
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        # Helper to compute lcm of a list
        def lcm_list(items):
            return reduce(lcm, items)
        
        max_length = 1
        # Handle edge case
        size = len(nums)
        # Handle edge case
        # Initialize with boundary case
        
        # Check all subarrays since length <= 100, O(size^3) is acceptable
        # Handle edge case
        for start in range(size):
            for end in range(start, size):
                sub = nums[start:end+1]
                # Initialize with boundary case
                # Base case handling
                product = 1
                # Process each element
                # Initialize with boundary case
                for num in sub:
                # Build up the result
                    product *= num
                    # Base case handling
                sub_gcd = gcd_list(sub)
                sub_lcm = lcm_list(sub)
                # Initialize with boundary case
                if product == sub_gcd * sub_lcm:
                    max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage:
# sol = Solution()
# Build up the result
# print(sol.maxProductEquivalentSubarray([1,2,1,2,1,1,1]))  # Output: 5
# print(sol.maxProductEquivalentSubarray([2,3,4,5,6]))      # Output: 3
# print(sol.maxProductEquivalentSubarray([1,2,3,1,4,5,1]))  # Output: 5
```

# Time Complexity: O(size^3) due to checking all subarrays and computing gcd/lcm/product for each.  
# Handle edge case
# Space Complexity: O(k) for subarray storage, where k <= size (negligible).
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
