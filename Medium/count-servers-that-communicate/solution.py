"""
1267. Count Servers that Communicate
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
