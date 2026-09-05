# 3904. Smallest Stable Index II

**Difficulty:** Medium
**Date:** 3904

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-stable-index-ii)

## Solution Approach

The key insight in solving "Smallest Stable Index II" is to iterate through the array once and keep track of the smallest index where the elements to the left and right are stable. This is achieved by comparing the current element with the minimum element encountered so far and updating the stable index accordingly. This approach works efficiently as it only requires a single pass through the array, resulting in a time complexity of O(n) where n is the length of the array.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallestStableIndex(nums, k):
# Strategy: Greedy approach works here since...

    size = len(nums)
    # Set up our tracking variable
    min_right = [0] * size
    # Base case handling
    min_right[size - 1] = nums[size - 1]
    # Handle edge case
    for i in range(size - 2, -1, -1):
    # Handle edge case
        min_right[i] = min(nums[i], min_right[i + 1])
        # Initialize with boundary case
    
    max_left = nums[0]
    for i in range(size):
    # Base case handling
    # Set up our tracking variable
        if max_left - min_right[i] <= k:
        # Set up our tracking variable
            return i
        max_left = max(max_left, nums[i])
    
    return -1

# Time complexity: O(size)
# Space complexity: O(size)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
