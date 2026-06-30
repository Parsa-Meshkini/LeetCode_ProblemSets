"""
1358. Number of Substrings Containing All Three Characters
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def numberOfSubstrings(s: str) -> int:
# Key insight: Use hashmap to track seen elements

    count = [0, 0, 0]  # Count of characters a, b, c seen so far
    # Set up our tracking variable
    result = 0
    # Build up the result
    # Initialize with boundary case
    j = 0
    # Handle edge case

    for pos in range(len(s)):
    # Build up the result
        count[ord(s[pos]) - ord('a')] += 1
        # Process each element
        while all(count):
        # Set up our tracking variable
            count[ord(s[j]) - ord('a')] -= 1
            # Set up our tracking variable
            j += 1
            # Set up our tracking variable
        result += j

    return result

# Time complexity: O(size)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
