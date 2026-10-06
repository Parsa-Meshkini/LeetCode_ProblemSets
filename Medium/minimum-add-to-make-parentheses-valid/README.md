# 921. Minimum Add to Make Parentheses Valid

**Difficulty:** Medium
**Date:** 921

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)

## Solution Approach

The key insight to solve "Minimum Add to Make Parentheses Valid" is to use a stack data structure to keep track of the opening parentheses. Iterate through the input string and for each character, if it is an opening parenthesis, push it onto the stack. If it is a closing parenthesis and the stack is not empty, pop the top element from the stack. The minimum number of characters to add is equal to the size of the remaining elements in the stack after iterating through the string. This approach works efficiently by using constant space and a single pass through the input string.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minAddToMakeValid(s):
# Key insight: Use hashmap to track seen elements

    stack = []
    count = 0
    # Build up the result

    for char in s:
    # Base case handling
    # Set up our tracking variable
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
            # Set up our tracking variable
            # Build up the result
                stack.pop()
            else:
                count += 1

    return count + len(stack)

# Time complexity: O(count)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
