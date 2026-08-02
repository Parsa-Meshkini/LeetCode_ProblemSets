# 877. Stone Game

**Difficulty:** Medium
**Date:** 877

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/stone-game)

## Solution Approach

In the Stone Game, the key insight is to use dynamic programming to calculate the maximum score the first player can achieve by considering all possible moves and their outcomes. This approach works efficiently because it avoids redundant calculations by storing and reusing intermediate results, allowing for a faster and optimal solution to the game.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def stoneGame(piles):
# Key insight: Use hashmap to track seen elements

    length = len(piles)
    # Handle edge case
    computed = [[0] * length for _ in range(length)]
    # Base case handling

    for i in range(length):
        computed[i][i] = piles[i]

    for l in range(2, length + 1):
    # Process each element
        for i in range(length - l + 1):
        # Set up our tracking variable
            end = i + l - 1
            # Set up our tracking variable
            computed[i][end] = max(piles[i] - computed[i + 1][end], piles[end] - computed[i][end - 1])
            # Handle edge case

    return computed[0][length - 1] > 0
```

Time complexity: O(length^2)
Space complexity: O(length^2)
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
