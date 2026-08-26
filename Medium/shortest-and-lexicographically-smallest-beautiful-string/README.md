# 2904. Shortest and Lexicographically Smallest Beautiful String

**Difficulty:** Medium
**Date:** 2904

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string)

## Solution Approach

The key insight for solving the "Shortest and Lexicographically Smallest Beautiful String" problem is to iteratively build the string by adding the lexicographically smallest character not already present in the current substring. This approach guarantees that the resulting string is both the shortest and lexicographically smallest beautiful string possible. This method works efficiently because it optimally selects characters to minimize the length and maintain lexicographical order.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def shortestBeautifulString(s, k):
# Process each element
# Key insight: Use hashmap to track seen elements

    count = len(s)
    # Set up our tracking variable
    result = ""
    for current in range(count):
    # Set up our tracking variable
        cnt = 0
        for next_idx in range(current, count):
            if s[next_idx] == "1":
            # Base case handling
                cnt += 1
                # Build up the result
            if cnt == k:
            # Set up our tracking variable
                if not result or s[current:next_idx+1] < result:
                # Handle edge case
                    result = s[current:next_idx+1]
                    # Base case handling
                break
    return result

# Time complexity: O(count^2)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
