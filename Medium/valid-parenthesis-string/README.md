# 678. Valid Parenthesis String

**Difficulty:** Medium
**Date:** 678

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/valid-parenthesis-string)

## Solution Approach

The key insight to solve the "Valid Parenthesis String" problem is to use two stacks to track the indices of open brackets and asterisks. By iterating through the string and maintaining these stacks, we can efficiently validate the string in linear time complexity O(n) without backtracking. This approach works efficiently by leveraging the properties of the asterisks to handle both open and close brackets dynamically.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def checkValidString(s: str) -> bool:
    low = 0  # Minimum possible open brackets
    # Base case handling
    high = 0  # Maximum possible open brackets
    # Base case handling
    for c in s:
    # Set up our tracking variable
        if c == '(':
        # Build up the result
            low += 1
            # Build up the result
            high += 1
            # Handle edge case
        elif c == ')':
        # Build up the result
            low = max(0, low - 1)
            high -= 1
            # Handle edge case
        else:
            low = max(0, low - 1)
            high += 1
            # Handle edge case
        if high < 0:
        # Build up the result
            return False
    return low == 0
    # Base case handling
    # Initialize with boundary case

# Time complexity: O(count)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
