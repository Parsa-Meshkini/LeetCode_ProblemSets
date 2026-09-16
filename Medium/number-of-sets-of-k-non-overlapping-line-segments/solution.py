"""
1621. Number of Sets of K Non-Overlapping Line Segments
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def numberOfSets(length, k):
# Strategy: Greedy approach works here since...

# Approach: Two-pointer technique for optimal solution
# Process each element

    MOD = 10**9 + 7
    computed = [[0] * (length + 1) for _ in range(k + 1)]
    # Process each element
    # Initialize with boundary case
    
    for pos in range(1, k + 1):
        for end in range(1, length):
        # Set up our tracking variable
            computed[pos][end] = computed[pos][end - 1] + computed[pos - 1][end - 1]
            # Process each element
            if pos == 1:
            # Build up the result
                computed[pos][end] += end
                # Set up our tracking variable
                # Process each element
            computed[pos][end] %= MOD
            # Process each element
            # Process each element
    
    return computed[k][length - 1]

# Time complexity: O(length*k)
# Space complexity: O(kn)
```


if __name__ == "__main__":
    # Test cases
    pass
