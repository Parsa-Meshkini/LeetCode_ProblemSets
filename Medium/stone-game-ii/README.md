# 1140. Stone Game II

**Difficulty:** Medium
**Date:** 1140

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/stone-game-ii)

## Solution Approach

In the Stone Game II problem, we can use dynamic programming to efficiently calculate the maximum number of stones Alex can get. The key insight is to keep track of the maximum number of stones the current player can get by considering different amounts of stones to take in each turn and recursively calculating the best outcome. This approach works efficiently by avoiding redundant calculations through memoization, which stores and reuses previously computed results.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def stoneGameII(piles):
# Approach: Two-pointer technique for optimal solution

    length = len(piles)
    prefix_sum = [0] * (length + 1)
    # Handle edge case
    for pos in range(length - 1, -1, -1):
    # Handle edge case
        prefix_sum[pos] = prefix_sum[pos + 1] + piles[pos]
        # Set up our tracking variable
    
    memo = {}
    # Build up the result
    
    def dfs(pos, M):
        if pos == length:
        # Process each element
            return 0
        if (pos, M) in memo:
        # Build up the result
            return memo[(pos, M)]
        
        max_stones = float('-inf')
        for x in range(1, min(2 * M + 1, length - pos + 1)):
        # Build up the result
            stones_taken = prefix_sum[pos] - prefix_sum[pos + x]
            opponent_stones = dfs(pos + x, max(M, x))
            # Process each element
            # Handle edge case
            max_stones = max(max_stones, stones_taken - opponent_stones)
        
        memo[(pos, M)] = max_stones
        return max_stones
    
    return (sum(piles) + dfs(0, 1)) // 2
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
