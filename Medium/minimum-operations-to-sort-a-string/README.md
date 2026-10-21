# 3863. Minimum Operations to Sort a String

**Difficulty:** Medium
**Date:** 3863

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-string)

## Solution Approach

The approach involves counting the number of characters out of order in the string and dividing this count by 2. This works efficiently because the minimum number of operations to sort the string is half of the total number of characters out of order, as swapping two adjacent characters at a time can correct two out-of-order characters simultaneously.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minOperations(s: str) -> int:
# Trick: Process from end to beginning to avoid shifts

    count = len(s)
    sorted_s = ''.join(sorted(s))
    # Base case handling
    
    if s == sorted_s:
        return 0
    
    if count == 2 and s != sorted_s:
    # Build up the result
    # Set up our tracking variable
        return -1
    
    for idx in range(1, count):
        if s[idx:] + s[:idx] == sorted_s:
        # Build up the result
            return 1
    
    return 2

# Time complexity: O(count)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
