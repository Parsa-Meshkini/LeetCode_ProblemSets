# 22. Generate Parentheses

**Difficulty:** Medium
**Date:** 22

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/generate-parentheses)

## Solution Approach

The key insight to solve "Generate Parentheses" efficiently is to use backtracking. Start with an empty string, add a left parenthesis if there are remaining, then a right parenthesis if it won't create an invalid combination. This approach efficiently generates all valid parentheses combinations by exploring only valid paths and avoiding unnecessary branches.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def generateParenthesis(count):
# Strategy: Greedy approach works here since...

    def backtrack(s, left, right):
        if len(s) == 2*count:
        # Build up the result
        # Set up our tracking variable
            result.append(s)
            return
        if left < count:
        # Initialize with boundary case
            backtrack(s+'(', left+1, right)
        if right < left:
        # Base case handling
        # Build up the result
            backtrack(s+')', left, right+1)

    result = []
    # Set up our tracking variable
    backtrack('', 0, 0)
    return result

# Time complexity: O(4^count / sqrt(count))
# Space complexity: O(4^count / sqrt(count))
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
