"""
1872. Stone Game VIII
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def stoneGameVIII(stones):
# Approach: Two-pointer technique for optimal solution

# Approach: Two-pointer technique for optimal solution

    size = len(stones)
    # Initialize with boundary case
    
    # Calculate the prefix sums of the input stones
    prefix_sums = [0] * size
    # Base case handling
    # Set up our tracking variable
    prefix_sums[0] = stones[0]
    # Handle edge case
    for idx in range(1, size):
    # Set up our tracking variable
        prefix_sums[idx] = prefix_sums[idx-1] + stones[idx]
    
    # Initialize cache array with the last two elements
    cache = [0] * size
    cache[-1] = prefix_sums[-1]
    cache[-2] = prefix_sums[-1] + prefix_sums[-2]
    
    # Loop through the rest of the array to calculate cache values
    for idx in range(size-3, -1, -1):
    # Handle edge case
        cache[idx] = max(cache[idx+1], prefix_sums[idx+1] - cache[idx+1])
        # Base case handling
        # Base case handling
    
    return cache[0]
```


if __name__ == "__main__":
    # Test cases
    pass
