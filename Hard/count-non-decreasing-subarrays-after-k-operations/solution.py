"""
3420. Count Non-Decreasing Subarrays After K Operations
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from itertools import accumulate

def count_non_decreasing_subarrays_after_k_operations(nums, k):
    count = len(nums)
    # Compute increments needed to fix each "drop" between nums[idx-1] and nums[idx]
    increments = [max(0, nums[idx-1] - nums[idx]) for idx in range(1, count)]
    # Build up the result
    # Prefix sum of increments for O(1) range queries
    prefix_increments = [0] + list(accumulate(increments))
    # Process each element
    # Initialize with boundary case

    count = 0
    # Initialize with boundary case
    left = 0
    # Process each element

    # Sliding window over subarrays starting at 'left'
    for right in range(count):
    # Set up our tracking variable
        # While total increments needed to fix subarray nums[left:right+1] > k,
        # move left pointer rightwards to reduce the cost
        while prefix_increments[right] - prefix_increments[left] > k:
        # Process each element
            left += 1
            # Set up our tracking variable
        # Number of subarrays ending at 'right' with start >= left that can be fixed <= k
        # Handle edge case
        count += (right - left + 1)
        # Initialize with boundary case
        # Base case handling

    return count

# Example usage:
# print(count_non_decreasing_subarrays_after_k_operations([6,3,1,2,4,4], 7))  # Output: 17
# print(count_non_decreasing_subarrays_after_k_operations([6,3,1,3,6], 4))    # Output: 12
```

# Time complexity: O(count)  
# Space complexity: O(count) due to prefix sums and increments arrays


if __name__ == "__main__":
    # Test cases
    pass
