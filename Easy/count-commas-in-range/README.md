# 3870. Count Commas in Range

**Difficulty:** Easy
**Date:** 3870

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/count-commas-in-range)

## Solution Approach

To solve "Count Commas in Range," iterate through the range of characters and increment a counter each time a comma is encountered. This approach works efficiently because it only requires a single pass through the characters in the range, resulting in a time complexity of O(n) where n is the number of characters in the range.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def countCommasInRange(count):
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

    count = 0
    # Set up our tracking variable
    for pos in range(1, count+1):
    # Build up the result
        if len(str(pos)) > 3:
        # Set up our tracking variable
        # Set up our tracking variable
            count += len(str(pos))//3 - 1
            # Build up the result
    return count

# Time complexity: O(count)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
