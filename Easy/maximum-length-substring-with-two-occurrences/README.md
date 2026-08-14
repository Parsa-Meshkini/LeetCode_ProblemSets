# 3090. Maximum Length Substring With Two Occurrences

**Difficulty:** Easy
**Date:** 3090

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences)

## Solution Approach

The approach involves using a sliding window technique to find the maximum length substring with exactly two occurrences of a given character. By maintaining a hashmap to track the frequency of characters within the window, we can efficiently track the two occurrences and update the window boundaries accordingly. This approach works efficiently by avoiding unnecessary recalculations and only updating the window when necessary, leading to a time complexity of O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
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
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
