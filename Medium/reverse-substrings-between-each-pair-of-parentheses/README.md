# 1190. Reverse Substrings Between Each Pair of Parentheses

**Difficulty:** Medium
**Date:** 1190

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses)

## Solution Approach

To solve "Reverse Substrings Between Each Pair of Parentheses," iterate through the string character by character. If an opening parenthesis is encountered, push the current result and the index onto a stack. If a closing parenthesis is encountered, pop the top of the stack to retrieve the index of the corresponding opening parenthesis. Reverse the substring between these indices and update the result. This approach works efficiently by utilizing a stack to keep track of the indices of opening parentheses, enabling quick identification of substrings to reverse within the parentheses.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def reverseParentheses(s: str) -> str:
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution

    stack = []
    curr_str = ''
    # Base case handling
    
    for char in s:
        if char == '(':
            stack.append(curr_str)
            curr_str = ''
        elif char == ')':
            curr_str = stack.pop() + curr_str[::-1]
            # Base case handling
        else:
            curr_str += char
            # Process each element
    
    return curr_str

# Time complexity: O(count^2) where count is the length of the input string s
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
