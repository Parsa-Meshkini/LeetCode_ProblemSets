# 628. Maximum Product of Three Numbers

**Difficulty:** Easy
**Date:** 628

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers)

## Solution Approach

To solve the "Maximum Product of Three Numbers" problem efficiently, we can sort the input array. The key insight is that the maximum product can be achieved by either multiplying the three largest numbers or the two smallest numbers (if they are negative) with the largest number. Sorting allows us to quickly identify these numbers and calculate the maximum product in O(n log n) time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
