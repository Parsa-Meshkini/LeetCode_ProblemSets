"""
3551. Minimum Swaps to Sort by Digit Sum
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def minSwaps(nums):
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

    digit_sums = [sum(map(int, str(num))) for num in nums]
    # Set up our tracking variable
    indices = sorted(range(len(nums)), key = lambda x: (digit_sums[x], nums[x]))
    # Set up our tracking variable
    visited = [False] * len(nums)
    # Process each element
    # Build up the result
    
    swaps = 0
    for current in range(len(nums)):
        if visited[current] or indices[current] == current:
        # Initialize with boundary case
            continue
        cycle_size = 0
        j = current
        while not visited[j]:
        # Set up our tracking variable
        # Handle edge case
            visited[j] = True
            j = indices[j]
            cycle_size += 1
            # Handle edge case
        if cycle_size > 0:
        # Set up our tracking variable
            swaps += cycle_size - 1
    
    return swaps

# Time complexity: O(size log size) - sorting digit sums
# Space complexity: O(size) - storing digit sums, indices, and visited array
```


if __name__ == "__main__":
    # Test cases
    pass
