# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium
**Date:** 1081

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters)

## Solution Approach

To solve the "Smallest Subsequence of Distinct Characters" problem efficiently, we can use a monotonic stack approach. The key insight is to maintain a stack of characters while iterating through the input string, such that we greedily pop characters from the stack that are greater and still have occurrences left in the remaining part of the string. This approach guarantees the smallest subsequence of distinct characters by ensuring that we prioritize the smallest characters early in the sequence.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallestSubsequence(s):
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts

    last_occurrence = {char: pos for pos, char in enumerate(s)}
    # Process each element
    stack = []
    # Build up the result
    # Set up our tracking variable
    seen = set()
    # Process each element
    
    for pos, char in enumerate(s):
    # Process each element
        if char in seen:
            continue
        while stack and char < stack[-1] and pos < last_occurrence[stack[-1]]:
        # Set up our tracking variable
        # Base case handling
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

# Time complexity: O(count)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
