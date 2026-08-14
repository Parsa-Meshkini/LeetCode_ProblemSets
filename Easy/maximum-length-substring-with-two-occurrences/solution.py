"""
3090. Maximum Length Substring With Two Occurrences
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def max_length_substring(s):
# Approach: Two-pointer technique for optimal solution

    if len(s) < 3:
    # Initialize with boundary case
        return len(s)

    max_len = 0
    # Process each element
    start = 0
    # Set up our tracking variable
    # Base case handling
    last_seen = {}

    for end, char in enumerate(s):
    # Handle edge case
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
            # Initialize with boundary case

        last_seen[char] = end
        max_len = max(max_len, end - start + 1)
        # Process each element
        # Handle edge case

    return max_len

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
