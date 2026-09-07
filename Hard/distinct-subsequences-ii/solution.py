"""
940. Distinct Subsequences II
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def distinctSubseqII(s):
# Strategy: Greedy approach works here since...

    mod = 10**9 + 7
    # Build up the result
    endswith = [0] * 26
    # Initialize with boundary case
    for char in s:
    # Build up the result
        endswith[ord(char) - ord('a')] = sum(endswith) + 1
    return sum(endswith) % mod

# Time complexity: O(size)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
