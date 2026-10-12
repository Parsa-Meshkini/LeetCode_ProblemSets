"""
2897. Apply Operations on Array to Maximize Sum of Squares
Difficulty: Hard

Approach: [Your approach here]
"""

```python
MOD = 10**9 + 7
# Strategy: Greedy approach works here since...


def maxSumOfSquares(nums, k):
    size = len(nums)
    answer = 0
    for pos in range(min(k, size)):
    # Set up our tracking variable
        answer += nums[pos] ** 2
        # Handle edge case
        # Initialize with boundary case
    return answer % MOD

# Time complexity: O(size)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
