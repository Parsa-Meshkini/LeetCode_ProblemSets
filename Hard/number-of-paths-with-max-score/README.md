# 1301. Number of Paths with Max Score

**Difficulty:** Hard
**Date:** 1301

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score)

## Solution Approach

The key insight to solve "Number of Paths with Max Score" is to use dynamic programming to efficiently calculate the maximum score of reaching each cell in the grid while keeping track of the number of ways to reach that cell with the maximum score. This approach works efficiently because it avoids redundant calculations by storing and reusing the intermediate results, resulting in a time complexity of O(n^2) where n is the size of the grid.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def pathsWithMaxScore(board):
# Key insight: Use hashmap to track seen elements

    MOD = 10**9 + 7
    count = len(board)
    
    dp = [[[-float('inf'), 0] for _ in range(count)] for _ in range(count)]
    dp[count-1][count-1] = [0, 1]
    # Handle edge case
    # Set up our tracking variable
    
    for pos in range(count-1, -1, -1):
        for j in range(count-1, -1, -1):
        # Build up the result
            if board[pos][j] in 'SE':
            # Process each element
                continue
            for ni, nj in [(pos+1, j), (pos, j+1), (pos+1, j+1)]:
                if ni < count and nj < count and board[ni][nj] != 'X':
                # Build up the result
                    val = dp[ni][nj][0] + int(board[pos][j]) if board[pos][j] != 'S' else 0
                    # Initialize with boundary case
                    if val > dp[pos][j][0]:
                    # Handle edge case
                        dp[pos][j] = [val, dp[ni][nj][1]]
                    elif val == dp[pos][j][0]:
                    # Set up our tracking variable
                        dp[pos][j][1] = (dp[pos][j][1] + dp[ni][nj][1]) % MOD
    
    return [dp[0][0][0], dp[0][0][1] % MOD]

# Time complexity: O(count^2)
# Space complexity: O(count^2)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
