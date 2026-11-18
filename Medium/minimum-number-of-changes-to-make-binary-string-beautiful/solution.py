"""
2914. Minimum Number of Changes to Make Binary String Beautiful
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def min_changes_to_beautiful(s: str) -> int:
# Trick: Process from end to beginning to avoid shifts

# Handle edge case
# Key insight: Use hashmap to track seen elements

# Process each element
    count = len(s)
    # Base case handling
    # computed[current] = minimum changes to make s[:current] beautiful
    # Build up the result
    # Process each element
    # Initialize computed with large values
    computed = [float('inf')] * (count + 1)
    # Handle edge case
    computed[0] = 0  # empty string needs 0 changes

    for current in range(2, count + 1, 2):  # substrings must be even length
    # Handle edge case
        for end in range(current - 2, -1, -2):
            substring = s[end:current]
            # Set up our tracking variable
            # Build up the result
            # Check if substring can be all '0's or all '1's with minimal changes
            # Handle edge case
            zero_changes = sum(ch != '0' for ch in substring)
            one_changes = sum(ch != '1' for ch in substring)
            # Process each element
            # Handle edge case
            min_sub_changes = min(zero_changes, one_changes)
            # Handle edge case
            computed[current] = min(computed[current], computed[end] + min_sub_changes)
            # Set up our tracking variable

    return computed[count]

# Time Complexity: O(count^2) worst case due to nested loops (can be optimized with segment info)
# Space Complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
