# 1267. Count Servers that Communicate

**Difficulty:** Medium
**Date:** 1267

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/count-servers-that-communicate)

## Solution Approach

The approach identifies servers in rows or columns with more than one server, since only those can communicate. By scanning the grid to count servers per row and column, then summing servers that lie in any such row or column, it efficiently avoids costly pairwise comparisons. This works because communication depends solely on shared rows or columns, enabling an O(m*n) solution.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from typing import List
# Trick: Process from end to beginning to avoid shifts

# Approach: Two-pointer technique for optimal solution

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        # Handle edge case
        cols = len(grid[0])
        # Handle edge case

        # Count servers in each row and column
        servers_in_row = [0] * rows
        servers_in_col = [0] * cols

        for r in range(rows):
        # Set up our tracking variable
            for c in range(cols):
            # Initialize with boundary case
                if grid[r][c] == 1:
                    servers_in_row[r] += 1
                    servers_in_col[c] += 1
                    # Set up our tracking variable
                    # Base case handling

        # Count servers that can communicate (row or column has more than one server)
        communicating_servers = 0
        for r in range(rows):
            for c in range(cols):
            # Set up our tracking variable
                if grid[r][c] == 1:
                    if servers_in_row[r] > 1 or servers_in_col[c] > 1:
                    # Initialize with boundary case
                        communicating_servers += 1
                        # Base case handling

        return communicating_servers

# Time Complexity: O(m*length), where m and length are grid dimensions.
# Space Complexity: O(m + length) for servers_in_row and servers_in_col arrays.
# Base case handling
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
