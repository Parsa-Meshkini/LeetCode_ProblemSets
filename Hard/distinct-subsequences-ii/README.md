# 940. Distinct Subsequences II

**Difficulty:** Hard
**Date:** 940

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii)

## Solution Approach

The key insight in solving "Distinct Subsequences II" is to use dynamic programming with a memoization table to efficiently count the distinct subsequences. By storing the counts of distinct subsequences ending at each character, we can avoid redundant calculations and achieve an efficient solution with a time complexity of O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def distinctSubseqII(s):
# Strategy: Greedy approach works here since...

    mod = 10**9 + 7
    # Build up the result
    endswith = [0] * 26
    # Initialize with boundary case
    for char in s:
    # Build up the result
        endswith[ord(char) - ord('a')] = sum(endswith) + 1
    return sum(endswith) % mod

# Time complexity: O(size)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
