# 3875. Construct Uniform Parity Array I

**Difficulty:** Easy
**Date:** 3875

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-i)

## Solution Approach

To solve "Construct Uniform Parity Array I," we start by creating an array with alternating 0s and 1s to achieve a uniform parity. This approach works efficiently because by simply setting every alternate element to 1, we can ensure a uniform parity throughout the array without needing to check individual elements for parity, resulting in a linear time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def canConstruct(nums1):
# Strategy: Greedy approach works here since...

    odd_count = 0
    # Initialize with boundary case
    for num in nums1:
    # Handle edge case
        if num % 2 == 1:
            odd_count += 1
    return odd_count == 0 or odd_count == len(nums1)
    # Process each element

# Time complexity: O(count)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
