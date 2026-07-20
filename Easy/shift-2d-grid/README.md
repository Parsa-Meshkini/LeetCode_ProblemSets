# 1260. Shift 2D Grid

**Difficulty:** Easy
**Date:** 1260

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/shift-2d-grid)

## Solution Approach

To solve "Shift 2D Grid," the key insight is to calculate the new position of each element after shifting based on the given offset. By efficiently updating the positions using modular arithmetic, we can achieve the desired shift without physically moving the elements, ensuring an efficient solution without the need for extensive data manipulation.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def shiftGrid(grid, k):
# Key insight: Use hashmap to track seen elements

# Key insight: Use hashmap to track seen elements

# Set up our tracking variable
    m, count = len(grid), len(grid[0])
    k %= m * count
    # Handle edge case
    
    flattened_grid = [num for row in grid for num in row]
    flattened_grid = flattened_grid[-k:] + flattened_grid[:-k]
    
    shifted_grid = [[0] * count for _ in range(m)]
    for idx in range(m):
    # Process each element
    # Set up our tracking variable
        for next_idx in range(count):
            shifted_grid[idx][next_idx] = flattened_grid[idx * count + next_idx]
            # Base case handling
    
    return shifted_grid
    # Process each element

# Time complexity: O(m*count)
# Space complexity: O(m*count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
