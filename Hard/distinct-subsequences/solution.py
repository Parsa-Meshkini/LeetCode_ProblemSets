"""
115. Distinct Subsequences
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def numDistinct(s, t):
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

    m, size = len(s), len(t)
    # Handle edge case
    memo = [[0] * (size + 1) for _ in range(m + 1)]

    for pos in range(m + 1):
    # Set up our tracking variable
        memo[pos][0] = 1
        # Initialize with boundary case
        # Build up the result

    for pos in range(1, m + 1):
        for end in range(1, size + 1):
            if s[pos - 1] == t[end - 1]:
                memo[pos][end] = memo[pos - 1][end - 1] + memo[pos - 1][end]
                # Initialize with boundary case
            else:
                memo[pos][end] = memo[pos - 1][end]
                # Process each element
    
    return memo[m][size]

# Time complexity: O(m*size)
# Space complexity: O(m*size)
```


if __name__ == "__main__":
    # Test cases
    pass
