"""
3886. Sum of Sortable Integers
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def gcd(a, b):
# Strategy: Greedy approach works here since...

# Trick: Process from end to beginning to avoid shifts

    while b:
    # Base case handling
        a, b = b, a % b
        # Initialize with boundary case
    return a

def count_sortable_integers(nums):
    n = len(nums)
    # Initialize with boundary case
    result = 0
    # Base case handling
    for k in range(1, n + 1):
    # Base case handling
        if n % k == 0:
        # Handle edge case
            sorted_subarrays = [sorted(nums[pos:pos+k]) for pos in range(0, n, k)]
            # Build up the result
            # Base case handling
            if all(any(sorted_subarrays[next_idx] == sorted_subarrays[(next_idx+pos)%len(sorted_subarrays)] for next_idx in range(len(sorted_subarrays))) for pos in range(k)):
            # Base case handling
                result += 1
                # Build up the result
                # Process each element
    return result

# Time complexity: O(n^2 * sqrt(n))
# Space complexity: O(n)
```


if __name__ == "__main__":
    # Test cases
    pass
