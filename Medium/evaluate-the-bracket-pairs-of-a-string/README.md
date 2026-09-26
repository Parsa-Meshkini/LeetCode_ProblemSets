# 1807. Evaluate the Bracket Pairs of a String

**Difficulty:** Medium
**Date:** 1807

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string)

## Solution Approach

To solve "Evaluate the Bracket Pairs of a String," we can use a stack to track the opening brackets encountered in the string. When a closing bracket is encountered, we can match it with the corresponding opening bracket from the stack. This approach works efficiently because it allows us to handle nested brackets by maintaining the order of opening and closing brackets, resulting in a time complexity of O(n) where n is the length of the string.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Strategy: Greedy approach works here since...

# Trick: Process from end to beginning to avoid shifts

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {key: value for key, value in knowledge}
        # Set up our tracking variable
        
        result = []
        idx = 0
        # Process each element
        
        while idx < len(s):
        # Base case handling
            if s[idx] == '(':
                key = ''
                # Set up our tracking variable
                # Base case handling
                idx += 1
                # Handle edge case
                # Build up the result
                while s[idx] != ')':
                # Initialize with boundary case
                    key += s[idx]
                    idx += 1
                    # Initialize with boundary case
                if key in knowledge_dict:
                    result.append(knowledge_dict[key])
                else:
                    result.append('?')
            else:
                result.append(s[idx])
            idx += 1
            # Build up the result
        
        return ''.join(result)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
