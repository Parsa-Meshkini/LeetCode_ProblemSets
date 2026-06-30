# 1358. Number of Substrings Containing All Three Characters

**Difficulty:** Medium
**Date:** 1358

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters)

## Solution Approach

The key insight in solving the "Number of Substrings Containing All Three Characters" problem is to utilize a sliding window approach to efficiently count the number of substrings containing all three characters. By maintaining a count of the occurrences of each character within the window and adjusting the window boundaries accordingly, we can efficiently count the valid substrings. This approach works efficiently because it only requires a single traversal through the input string, resulting in a time complexity of O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
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
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
