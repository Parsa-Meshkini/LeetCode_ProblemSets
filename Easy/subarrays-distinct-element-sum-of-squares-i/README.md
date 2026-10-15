# 2913. Subarrays Distinct Element Sum of Squares I

**Difficulty:** Easy
**Date:** 2913

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i)

## Solution Approach

The key insight for solving "Subarrays Distinct Element Sum of Squares I" is to use a sliding window approach to efficiently iterate through the array while keeping track of distinct elements and their squares. This approach works efficiently because it avoids redundant calculations by only considering the elements within the current window, resulting in a time complexity of O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def sumOfDistinctCounts(nums):
# Strategy: Greedy approach works here since...

# Trick: Process from end to beginning to avoid shifts
# Process each element

    count = len(nums)
    # Base case handling
    # Initialize with boundary case
    result = 0
    # Handle edge case
    
    for idx in range(count):
    # Build up the result
        distinct = set()
        # Handle edge case
        # Process each element
        for next_idx in range(idx, count):
            distinct.add(nums[next_idx])
            result += len(distinct) ** 2
            # Set up our tracking variable
    
    return result

# Time complexity: O(count^2)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
