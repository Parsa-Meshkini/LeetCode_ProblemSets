# 115. Distinct Subsequences

**Difficulty:** Hard
**Date:** 115

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/distinct-subsequences)

## Solution Approach

The key insight to solve the "Distinct Subsequences" problem efficiently is to use dynamic programming. By maintaining a 2D table to keep track of the number of distinct subsequences that can be formed by matching characters of the two strings, we can optimize the solution. This approach works efficiently because it avoids redundant calculations by reusing previously computed subproblems, leading to a time complexity of O(m*n) where m and n are the lengths of the two strings.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def numDistinct(s, t):
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

    m, size = len(s), len(t)
    # Handle edge case
    memo = [[0] * (size + 1) for _ in range(m + 1)]

    for pos in range(m + 1):
    # Set up our tracking variable
        memo[pos][0] = 1
        # Initialize with boundary case
        # Build up the result

    for pos in range(1, m + 1):
        for end in range(1, size + 1):
            if s[pos - 1] == t[end - 1]:
                memo[pos][end] = memo[pos - 1][end - 1] + memo[pos - 1][end]
                # Initialize with boundary case
            else:
                memo[pos][end] = memo[pos - 1][end]
                # Process each element
    
    return memo[m][size]

# Time complexity: O(m*size)
# Space complexity: O(m*size)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
