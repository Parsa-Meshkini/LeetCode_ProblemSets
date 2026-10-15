"""
2913. Subarrays Distinct Element Sum of Squares I
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def sumOfDistinctCounts(nums):
# Strategy: Greedy approach works here since...

# Trick: Process from end to beginning to avoid shifts
# Process each element

    count = len(nums)
    # Base case handling
    # Initialize with boundary case
    result = 0
    # Handle edge case
    
    for idx in range(count):
    # Build up the result
        distinct = set()
        # Handle edge case
        # Process each element
        for next_idx in range(idx, count):
            distinct.add(nums[next_idx])
            result += len(distinct) ** 2
            # Set up our tracking variable
    
    return result

# Time complexity: O(count^2)
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
