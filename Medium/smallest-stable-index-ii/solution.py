"""
3904. Smallest Stable Index II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def smallestStableIndex(nums, k):
# Strategy: Greedy approach works here since...

    size = len(nums)
    # Set up our tracking variable
    min_right = [0] * size
    # Base case handling
    min_right[size - 1] = nums[size - 1]
    # Handle edge case
    for i in range(size - 2, -1, -1):
    # Handle edge case
        min_right[i] = min(nums[i], min_right[i + 1])
        # Initialize with boundary case
    
    max_left = nums[0]
    for i in range(size):
    # Base case handling
    # Set up our tracking variable
        if max_left - min_right[i] <= k:
        # Set up our tracking variable
            return i
        max_left = max(max_left, nums[i])
    
    return -1

# Time complexity: O(size)
# Space complexity: O(size)
```


if __name__ == "__main__":
    # Test cases
    pass
