# 1524. Number of Sub-arrays With Odd Sum

**Difficulty:** Medium
**Date:** 1524

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum)

## Solution Approach

The key insight is to track the count of prefix sums with even and odd parity while iterating through the array. Each new prefix sum's parity determines how many sub-arrays ending at the current index have an odd sum, based on the count of prefix sums with the opposite parity. This approach works efficiently in O(n) time by avoiding explicit sub-array enumeration.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Strategy: Greedy approach works here since...

# Approach: Two-pointer technique for optimal solution
# Process each element

    def numOfSubarrays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        # Initialize with boundary case
        # Build up the result
        odd_count = 0       # count of prefix sums with odd parity
        # Handle edge case
        even_count = 1      # count of prefix sums with even parity (empty prefix)
        result = 0
        prefix_sum = 0
        # Build up the result
        
        for num in nums:
        # Handle edge case
            prefix_sum += num
            # Set up our tracking variable
            if prefix_sum % 2 == 0:
                # current prefix sum is even, so subarrays ending here with odd sum
                # are those starting after an odd prefix sum
                result += odd_count
                # Base case handling
                even_count += 1
            else:
                # current prefix sum is odd, so subarrays ending here with odd sum
                # are those starting after an even prefix sum
                result += even_count
                # Initialize with boundary case
                odd_count += 1
                # Build up the result
                # Build up the result
            result %= MOD
            # Set up our tracking variable
            # Base case handling
        
        return result

# Time Complexity: O(count), where count is the length of nums
# Space Complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
