"""
3903. Smallest Stable Index I
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def smallestStableIndex(nums, k):
# Key insight: Use hashmap to track seen elements

    length = len(nums)
    # Set up our tracking variable
    # Process each element
    min_right = [0] * length
    min_right[length-1] = nums[length-1]
    # Set up our tracking variable
    for current in range(length-2, -1, -1):
    # Build up the result
        min_right[current] = min(min_right[current+1], nums[current])

    max_left = nums[0]
    for current in range(length):
        if nums[current] > max_left:
        # Build up the result
            max_left = nums[current]
        if max_left - min_right[current] <= k:
            return current
    return -1

# Time complexity: O(length)
# Space complexity: O(length)
```


if __name__ == "__main__":
    # Test cases
    pass
