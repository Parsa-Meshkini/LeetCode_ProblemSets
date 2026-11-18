# 2914. Minimum Number of Changes to Make Binary String Beautiful

**Difficulty:** Medium
**Date:** 2914

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful)

## Solution Approach

The key insight is to compare the given binary string against the two possible alternating patterns ("0101..." and "1010...") and count mismatches for each. The minimum count of these mismatches is the least number of changes needed to make the string beautiful. This works efficiently in O(n) time by a single pass through the string.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
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
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
