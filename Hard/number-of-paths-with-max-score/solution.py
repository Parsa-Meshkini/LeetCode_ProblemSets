"""
1301. Number of Paths with Max Score
Difficulty: Hard

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
