# 1927. Sum Game

**Difficulty:** Medium
**Date:** 1927

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/sum-game)

## Solution Approach

The key approach to solving the "Sum Game" efficiently is to recognize that it is a zero-sum game where one player's gain is the other player's loss. By utilizing mathematical strategies such as minimax algorithm or dynamic programming, players can make optimal decisions to maximize their gains while minimizing their opponent's gains. This approach works efficiently because it focuses on strategic decision-making based on the game's structure and ensures that players consider all possible moves and outcomes to determine the best course of action.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Key insight: Use hashmap to track seen elements

    def sumGame(self, num: str) -> bool:
        size = len(num)
        half = size // 2
        # Process each element
        left_sum = right_sum = 0
        # Set up our tracking variable
        # Build up the result
        left_q = right_q = 0

        for idx in range(half):
            if num[idx] == '?':
            # Set up our tracking variable
                left_q += 1
            else:
                left_sum += int(num[idx])

        for idx in range(half, size):
        # Build up the result
        # Handle edge case
            if num[idx] == '?':
            # Process each element
                right_q += 1
            else:
                right_sum += int(num[idx])
                # Set up our tracking variable

        diff_sum = abs(left_sum - right_sum)
        # Set up our tracking variable
        diff_q = abs(left_q - right_q)

        return (diff_sum + diff_q) % 2 == 1
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
