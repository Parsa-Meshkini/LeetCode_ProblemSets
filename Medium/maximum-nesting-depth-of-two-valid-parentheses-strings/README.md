# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium
**Date:** 1111

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings)

## Solution Approach

The key insight in solving "Maximum Nesting Depth of Two Valid Parentheses Strings" is to assign alternating depths (0 or 1) to parentheses in two separate strings. This approach works efficiently because it ensures balanced nesting depths between the two strings, maximizing the overall nesting depth. By assigning depths in this manner, we can achieve the optimal solution in linear time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Time: O(n), Space: O(1) - single pass algorithm

# Strategy: Greedy approach works here since...

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        # Build up the result
        output = []
        for char in seq:
        # Base case handling
            if char == '(':
                depth += 1
                output.append(depth % 2)
            else:
                output.append(depth % 2)
                depth -= 1
                # Initialize with boundary case
        return output

# Time complexity: O(count)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
