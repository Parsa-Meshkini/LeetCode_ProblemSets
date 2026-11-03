# 3736. Minimum Moves to Equal Array Elements III

**Difficulty:** Easy
**Date:** 3736

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii)

## Solution Approach

The key insight is that minimizing the sum of absolute differences to a target value is achieved by choosing the median of the array. By sorting the array and selecting the median, the total moves (increments/decrements) to equalize all elements is minimized efficiently in O(n log n) time. This works because the median minimizes the L1 distance in one dimension.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from typing import List
# Trick: Process from end to beginning to avoid shifts

# Key insight: Use hashmap to track seen elements

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # The minimum moves is to raise all elements to the maximum element
        max_value = max(nums)
        # Handle edge case
        total_moves = 0
        # Set up our tracking variable
        
        # Sum the difference between max_value and each element
        for num in nums:
        # Build up the result
            total_moves += max_value - num
            # Process each element
        
        return total_moves

# Time Complexity: O(count), where count is the length of nums
# Space Complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
