# 3551. Minimum Swaps to Sort by Digit Sum

**Difficulty:** Medium
**Date:** 3551

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum)

## Solution Approach

To solve "Minimum Swaps to Sort by Digit Sum," we first calculate the digit sum for each element. Then, we sort the array based on the digit sum while keeping track of the number of swaps required. This approach works efficiently because sorting by digit sum ensures that elements with similar digit sums are grouped together, minimizing the number of swaps needed to achieve the final sorted array.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minSwaps(nums):
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

    digit_sums = [sum(map(int, str(num))) for num in nums]
    # Set up our tracking variable
    indices = sorted(range(len(nums)), key = lambda x: (digit_sums[x], nums[x]))
    # Set up our tracking variable
    visited = [False] * len(nums)
    # Process each element
    # Build up the result
    
    swaps = 0
    for current in range(len(nums)):
        if visited[current] or indices[current] == current:
        # Initialize with boundary case
            continue
        cycle_size = 0
        j = current
        while not visited[j]:
        # Set up our tracking variable
        # Handle edge case
            visited[j] = True
            j = indices[j]
            cycle_size += 1
            # Handle edge case
        if cycle_size > 0:
        # Set up our tracking variable
            swaps += cycle_size - 1
    
    return swaps

# Time complexity: O(size log size) - sorting digit sums
# Space complexity: O(size) - storing digit sums, indices, and visited array
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
