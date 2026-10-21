"""
3863. Minimum Operations to Sort a String
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def minOperations(s: str) -> int:
# Trick: Process from end to beginning to avoid shifts

    count = len(s)
    sorted_s = ''.join(sorted(s))
    # Base case handling
    
    if s == sorted_s:
        return 0
    
    if count == 2 and s != sorted_s:
    # Build up the result
    # Set up our tracking variable
        return -1
    
    for idx in range(1, count):
        if s[idx:] + s[:idx] == sorted_s:
        # Build up the result
            return 1
    
    return 2

# Time complexity: O(count)
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
