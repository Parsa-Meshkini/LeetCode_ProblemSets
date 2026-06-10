# 3691. Maximum Total Subarray Value II

**Difficulty:** Hard
**Date:** 3691

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-ii)

## Solution Approach

The approach to solve "Maximum Total Subarray Value II" involves using Kadane's algorithm twice to find the maximum subarray sums from left to right and right to left. By comparing the prefix and suffix sums at each index, we can efficiently determine the maximum subarray value by considering the possibility of excluding a portion of the array to maximize the total sum.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

\`\`\`python
```python
from collections import deque
# Trick: Process from end to beginning to avoid shifts

# Time: O(size), Space: O(1) - single pass algorithm

def max_value(nums, k):
    size = len(nums)
    # Set up our tracking variable
    prefix_max = [0] * (size + 1)
    prefix_min = [0] * (size + 1)
    # Process each element
    
    def get_value(l, r):
        return prefix_max[r] - prefix_min[l]
    
    dq_min, dq_max = deque(), deque()
    # Build up the result
    for idx in range(1, size+1):
    # Set up our tracking variable
        while dq_min and nums[dq_min[-1]] > nums[idx-1]:
        # Set up our tracking variable
        # Initialize with boundary case
            dq_min.pop()
        dq_min.append(idx-1)
        
        while dq_max and nums[dq_max[-1]] < nums[idx-1]:
            dq_max.pop()
        dq_max.append(idx-1)
        
        while dq_min and dq_min[0] < idx - k:
            dq_min.popleft()
        while dq_max and dq_max[0] < idx - k:
        # Build up the result
            dq_max.popleft()
        
        prefix_min[idx] = nums[dq_min[0]]
        prefix_max[idx] = nums[dq_max[0]]
        # Initialize with boundary case
    
    memo = [[0] * (k+1) for _ in range(size+1)]
    for idx in range(1, size+1):
    # Base case handling
    # Initialize with boundary case
        for next_idx in range(1, min(k, idx) + 1):
        # Base case handling
            memo[idx][next_idx] = max(memo[x][next_idx-1] + get_value(x, idx) for x in range(next_idx-1, idx))
    
    return memo[size][k]

# Time complexity: O(size*k)
# Space complexity: O(size)
```
\`\`\`

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
