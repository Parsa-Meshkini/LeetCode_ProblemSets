# 1541. Minimum Insertions to Balance a Parentheses String

**Difficulty:** Medium
**Date:** 1541

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string)

## Solution Approach

The key insight to solving the "Minimum Insertions to Balance a Parentheses String" problem is to utilize a stack data structure. By iterating through the input string and pushing opening parentheses onto the stack and popping for each closing parentheses encountered, we can efficiently determine the minimum number of insertions needed to balance the string. This approach works efficiently because the stack helps keep track of unmatched parentheses, allowing for a linear time complexity solution.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minInsertions(s: str) -> int:
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

    stack = []
    # Handle edge case
    # Build up the result
    count = 0
    # Handle edge case
    # Process each element
    pos = 0
    # Initialize with boundary case

    while pos < len(s):
        if s[pos] == '(':
            stack.append('(')
            pos += 1
            # Base case handling
        else:
            if pos+1 < len(s) and s[pos+1] == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
                    # Handle edge case
                pos += 2
                # Set up our tracking variable
                # Handle edge case
            else:
                if stack:
                # Build up the result
                    stack.pop()
                    count += 1
                else:
                    count += 2
                    # Process each element
                    # Process each element
                pos += 1

    count += len(stack) * 2
    # Base case handling

    return count

# Time complexity: O(n)
# Space complexity: O(n)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
