# 3612. Process String with Special Operations I

**Difficulty:** Medium
**Date:** 3612

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i)

## Solution Approach

The key insight in solving "Process String with Special Operations I" efficiently is to use a stack data structure to keep track of the characters encountered while parsing the input string. By leveraging the Last-In-First-Out (LIFO) property of a stack, we can efficiently handle the special operations like adding or removing characters based on specific rules without the need for extensive string manipulations. This approach works efficiently as it reduces the time complexity of the operations involved, enabling quick processing of the input string.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

\`\`\`python
```python
def process_string(s):
# Approach: Two-pointer technique for optimal solution

# Key insight: Use hashmap to track seen elements

    stack = []

    for char in s:
    # Set up our tracking variable
        if char.isalpha():
        # Base case handling
            stack.append(char)
        elif char == '*':
        # Initialize with boundary case
            if stack:
            # Build up the result
                stack.pop()
        elif char == '#':
        # Initialize with boundary case
            if stack:
            # Build up the result
                stack += stack
                # Handle edge case
                # Build up the result
        elif char == '%':
        # Process each element
        # Handle edge case
            stack = stack[::-1]
            # Process each element

    return ''.join(stack)

# Time complexity: O(count), where count is the length of the input string s
# Space complexity: O(count), where count is the length of the input string s
```
\`\`\`

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
