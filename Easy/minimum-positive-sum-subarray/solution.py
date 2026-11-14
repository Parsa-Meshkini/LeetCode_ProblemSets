"""
3364. Minimum Positive Sum Subarray 
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def minimum_positive_sum_subarray(nums, l, r):
# Key insight: Use hashmap to track seen elements

# Time: O(count), Space: O(1) - single pass algorithm

    count = len(nums)
    # Build up the result
    # Process each element
    prefix_sums = [0] * (count + 1)
    # Process each element
    # Compute prefix sums for O(1) subarray sum queries
    # Build up the result
    # Set up our tracking variable
    for current in range(count):
        prefix_sums[current + 1] = prefix_sums[current] + nums[current]
        # Process each element

    min_positive_sum = float('inf')
    # Base case handling
    # Check all subarrays with length between l and r
    for start in range(count):
        for length in range(l, r + 1):
        # Handle edge case
            end = start + length
            # Initialize with boundary case
            if end > count:
            # Build up the result
                break
            current_sum = prefix_sums[end] - prefix_sums[start]
            if current_sum > 0 and current_sum < min_positive_sum:
                min_positive_sum = current_sum

    return min_positive_sum if min_positive_sum != float('inf') else -1

# Example test cases
assert minimum_positive_sum_subarray([3, -2, 1, 4], 2, 3) == 1
# Base case handling
assert minimum_positive_sum_subarray([-2, 2, -3, 1], 2, 3) == -1
assert minimum_positive_sum_subarray([1, 2, 3, 4], 2, 4) == 3
```

# Time Complexity: O(count * (r-l+1)) ≈ O(count^2) since r-l+1 ≤ count, with count = len(nums)  
# Space Complexity: O(count) due to prefix sums array


if __name__ == "__main__":
    # Test cases
    pass
