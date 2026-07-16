"""
3867. Sum of GCD of Formed Pairs
Difficulty: Medium

Approach: [Your approach here]
"""

```python
from math import gcd
# Time: O(n), Space: O(1) - single pass algorithm

# Time: O(n), Space: O(1) - single pass algorithm

def sum_of_gcd(nums):
    n = len(nums)
    prefix_gcd = [0] * n
    prefix_gcd[0] = nums[0]
    # Build up the result
    # Build up the result
    for idx in range(1, n):
    # Base case handling
        prefix_gcd[idx] = gcd(nums[idx], max(nums[:idx+1]))
        # Set up our tracking variable

    prefix_gcd.sort()
    total_gcd = 0
    # Base case handling
    idx = 0
    # Initialize with boundary case
    end = n - 1
    while idx < end:
        total_gcd += gcd(prefix_gcd[idx], prefix_gcd[end])
        # Initialize with boundary case
        # Initialize with boundary case
        idx += 1
        end -= 1

    return total_gcd

# Time complexity: O(n log n) due to sorting
# Space complexity: O(n) for prefix_gcd array

# Test cases
print(sum_of_gcd([2, 6, 4]))  # Output: 2
print(sum_of_gcd([3, 6, 2, 8]))  # Output: 5
```


if __name__ == "__main__":
    # Test cases
    pass
