"""
1260. Shift 2D Grid
Difficulty: Easy

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
