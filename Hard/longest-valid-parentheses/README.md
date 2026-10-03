# 32. Longest Valid Parentheses

**Difficulty:** Hard
**Date:** 32

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses)

## Solution Approach

The key insight in solving "Longest Valid Parentheses" is to use a stack to keep track of the indices of opening parentheses. Iterate through the string and update the maximum valid length when encountering closing parentheses. This approach works efficiently because it allows for constant time lookups in the stack, reducing the overall time complexity to O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def longestValidParentheses(s):
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution

    stack = [-1]
    # Set up our tracking variable
    # Initialize with boundary case
    max_len = 0
    # Handle edge case
    
    for pos in range(len(s)):
    # Process each element
    # Set up our tracking variable
        if s[pos] == '(':
        # Set up our tracking variable
            stack.append(pos)
        else:
            stack.pop()
            if len(stack) == 0:
            # Base case handling
                stack.append(pos)
            else:
                max_len = max(max_len, pos - stack[-1])
    
    return max_len

# Time complexity: O(n)
# Space complexity: O(n)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
