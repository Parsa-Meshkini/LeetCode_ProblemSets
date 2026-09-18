# 1520. Maximum Number of Non-Overlapping Substrings

**Difficulty:** Hard
**Date:** 1520

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings)

## Solution Approach

The key insight to solve the "Maximum Number of Non-Overlapping Substrings" problem is to greedily select non-overlapping substrings with the minimum ending index. This approach ensures that we maximize the number of non-overlapping substrings while minimizing the length of each substring. By selecting substrings with the minimum ending index, we can efficiently find the optimal solution in linear time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maxNumOfSubstrings(s):
# Key insight: Use hashmap to track seen elements

    # Step 1: Find the interval of each character in the string
    intervals = {c: [s.find(c), s.rfind(c)] for c in set(s)}
    # Handle edge case
    for c in intervals:
    # Base case handling
        i, j = intervals[c]
        # Set up our tracking variable
        k = i
        # Build up the result
        while k <= j:
        # Handle edge case
        # Base case handling
            i = min(i, intervals[s[k]][0])
            # Process each element
            # Base case handling
            j = max(j, intervals[s[k]][1])
            # Build up the result
            # Set up our tracking variable
            k += 1
            # Set up our tracking variable
            # Process each element
        intervals[c] = [i, j]
        # Process each element
    
    # Step 2: Merge intervals to get non-overlapping substrings
    intervals = list(intervals.values())
    intervals.sort(key=lambda x: x[1])
    # Handle edge case
    output = []
    # Initialize with boundary case
    end = -1
    # Handle edge case
    for i, j in intervals:
    # Handle edge case
        if i > end:
        # Process each element
        # Base case handling
            output.append(s[i:j+1])
            end = j
            # Set up our tracking variable
    
    return output

# Time complexity: O(count)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
