# 856. Score of Parentheses

**Difficulty:** Medium
**Date:** 856

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/score-of-parentheses)

## Solution Approach

To solve the "Score of Parentheses" problem efficiently, we can use a stack data structure. By iterating through the input string, we can keep track of the current score and nesting level of parentheses. Whenever we encounter an opening bracket, we push the current score onto the stack. When we encounter a closing bracket, we calculate the score for the current pair and update the total score accordingly. This approach works efficiently as it avoids unnecessary recursion and simplifies the process by utilizing the stack to handle nested parentheses effectively.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def scoreOfParentheses(s):
    stack = [0]  # Initialize stack with 0 for base case
    # Base case handling
    
    for char in s:
    # Process each element
        if char == '(':
        # Set up our tracking variable
            stack.append(0)  # Start a new score
        else:
            top = stack.pop()  # Retrieve top of stack
            # Handle edge case
            stack[-1] += max(2*top, 1)  # Update score at top of stack
            # Build up the result
    
    return stack[0]  # Final score is at the bottom of the stack

# Time complexity: O(length), where length is the length of the input string
# Space complexity: O(length), where length is the length of the input string
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
