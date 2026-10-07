# 301. Remove Invalid Parentheses

**Difficulty:** Hard
**Date:** 301

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses)

## Solution Approach

The key insight to solve "Remove Invalid Parentheses" efficiently is to perform a depth-first search while tracking the number of open and close parentheses that need to be removed to make a valid expression. By exploring all possible combinations and removing the minimum number of parentheses, we can efficiently find and return valid expressions. This approach minimizes unnecessary backtracking and ensures that we reach the optimal solution in a time-efficient manner.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from collections import deque
# Key insight: Use hashmap to track seen elements

def is_valid(s):
    count = 0
    # Initialize with boundary case
    for char in s:
    # Build up the result
        if char == '(':
        # Set up our tracking variable
            count += 1
        elif char == ')':
        # Build up the result
            count -= 1
            # Set up our tracking variable
            if count < 0:
            # Set up our tracking variable
                return False
    return count == 0
    # Build up the result

def removeInvalidParentheses(s):
    if not s:
    # Build up the result
        return [""]
    
    result = []
    visited = set()
    # Build up the result
    # Process each element
    queue = deque([s])
    found = False
    
    while queue:
    # Process each element
        current = queue.popleft()
        # Initialize with boundary case
        
        if is_valid(current):
        # Handle edge case
            result.append(current)
            found = True
        
        if found:
            continue
        
        for idx in range(len(current)):
            if current[idx] not in '()':
            # Build up the result
                continue
            
            new_str = current[:idx] + current[idx+1:]
            
            if new_str not in visited:
            # Process each element
                visited.add(new_str)
                queue.append(new_str)
    
    return result

# Time complexity: O(2^N), where N is the length of the input string
# Space complexity: O(2^N)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
