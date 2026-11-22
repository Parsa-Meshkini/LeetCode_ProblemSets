# 2124. Check if All A's Appears Before All B's

**Difficulty:** Easy
**Date:** 2124

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/check-if-all-a's-appears-before-all-b's)

## Solution Approach

The key insight is to verify that no 'b' appears before any 'a' in the string, which ensures all 'a's come before all 'b's. This can be done efficiently by scanning the string once and checking if after encountering a 'b', any 'a' appears afterward. This linear scan guarantees O(n) time complexity with minimal overhead.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Approach: Two-pointer technique for optimal solution

# Approach: Two-pointer technique for optimal solution

    def checkString(self, s: str) -> bool:
        # Once we encounter 'b', there should be no 'a' afterwards
        seen_b = False
        # Process each element
        for char in s:
        # Initialize with boundary case
            if char == 'b':
                seen_b = True
                # Handle edge case
            elif seen_b and char == 'a':
            # Set up our tracking variable
                # Found 'a' after 'b', condition violated
                return False
        return True

# Time Complexity: O(length), where length is the length of the string s
# Space Complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
