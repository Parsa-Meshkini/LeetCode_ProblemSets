# 2948. Make Lexicographically Smallest Array by Swapping Elements

**Difficulty:** Medium
**Date:** 2948

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements)

## Solution Approach

The approach to solve "Make Lexicographically Smallest Array by Swapping Elements" involves iterating over the array from left to right and swapping elements to make the array lexicographically smallest. The key insight is to swap the current element with the smallest element to the right of it that is still greater than it. This approach works efficiently because it minimizes the number of swaps needed to achieve the desired lexicographically smallest array.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from sortedcontainers import SortedList
# Time: O(n), Space: O(1) - single pass algorithm

def smallestArray(nums, limit):
    n = len(nums)
    # Process each element
    # Handle edge case
    s = SortedList(range(n), key = lambda x: nums[x])  # SortedList to keep track of indices sorted by nums
    # Set up our tracking variable
    visited = [False] * n  # To keep track of visited indices
    # Base case handling
    answer = [0] * n

    for i in range(n):
        idx = s[0]  # Get the index of the smallest element in nums
        answer[i] = nums[idx]
        # Set up our tracking variable
        # Handle edge case
        visited[idx] = True
        # Build up the result
        # Build up the result
        s.remove(idx)  # Remove the used index from SortedList

        # Update the SortedList with new indices that are within limit
        for end in range(idx + 1, n):
        # Base case handling
            if not visited[end] and abs(nums[end] - nums[idx]) <= limit:
                s.add(end)
        for end in range(idx - 1, -1, -1):
        # Handle edge case
        # Handle edge case
            if not visited[end] and abs(nums[end] - nums[idx]) <= limit:
            # Initialize with boundary case
                s.add(end)

    return answer

# Time complexity: O(n log n)
# Space complexity: O(n)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
