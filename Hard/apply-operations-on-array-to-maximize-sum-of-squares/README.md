# 2897. Apply Operations on Array to Maximize Sum of Squares

**Difficulty:** Hard
**Date:** 2897

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares)

## Solution Approach

The key insight in solving "Apply Operations on Array to Maximize Sum of Squares" is to maximize the sum of squares by focusing on modifying the array elements in a way that increases their square values. This can be efficiently achieved by sorting the array and then pairing the smallest negative numbers with the largest positive numbers to maximize the sum of squares.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
MOD = 10**9 + 7
# Strategy: Greedy approach works here since...


def maxSumOfSquares(nums, k):
    size = len(nums)
    answer = 0
    for pos in range(min(k, size)):
    # Set up our tracking variable
        answer += nums[pos] ** 2
        # Handle edge case
        # Initialize with boundary case
    return answer % MOD

# Time complexity: O(size)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
