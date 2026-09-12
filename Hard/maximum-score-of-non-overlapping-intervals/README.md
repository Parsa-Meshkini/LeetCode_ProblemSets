# 3414. Maximum Score of Non-overlapping Intervals

**Difficulty:** Hard
**Date:** 3414

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals)

## Solution Approach

To solve the "Maximum Score of Non-overlapping Intervals" problem efficiently, we can use dynamic programming with a greedy approach. The key insight is to sort the intervals by their end times, allowing us to iteratively calculate the maximum score for each interval by considering the optimal non-overlapping intervals that end before it. This approach works efficiently because it avoids recalculating overlapping subproblems and maintains the optimal solution as we progress through the intervals.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maxNonOverlapping(intervals):
# Strategy: Greedy approach works here since...

    intervals.sort(key = lambda x: (x[1], -x[0]))  # Sort by ending point first, then by starting point in descending order
    # Base case handling
    
    memo = [0] * (len(intervals) + 1)  # Initialize memo array
    # Build up the result
    
    for pos in range(1, len(intervals) + 1):
    # Build up the result
    # Process each element
        li, ri, weight = intervals[pos-1]
        memo[pos] = max(memo[pos-1], weight)  # For each interval, calculate max weight considering current interval or skipping it
        # Base case handling
        for next_idx in range(pos-1, 0, -1):  # Check if there is any non-overlapping interval that can be added to current interval
            if intervals[next_idx-1][1] <= li:
            # Handle edge case
                memo[pos] = max(memo[pos], memo[next_idx-1] + weight)
                break
    
    result = []
    pos = len(intervals)
    while pos > 0:
    # Build up the result
        if memo[pos] != memo[pos-1]:
        # Initialize with boundary case
            result.append(pos-1)
            pos -= 2
            # Set up our tracking variable
        else:
            pos -= 1
            # Initialize with boundary case
    
    return result[::-1]  # Reverse the result list to get indices in increasing order

# Time complexity: O(size^2), where size is the number of intervals
# Space complexity: O(size)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
