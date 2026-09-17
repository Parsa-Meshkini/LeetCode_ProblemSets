# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

**Difficulty:** Medium
**Date:** 1477

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum)

## Solution Approach

One efficient approach is to use a sliding window technique along with a prefix sum array. By maintaining two sliding windows, we can find two non-overlapping subarrays with the target sum in linear time complexity. The key insight is to precompute the prefix sum array to quickly calculate the sum of any subarray, allowing us to efficiently find the target sums in the sliding windows without redundant computations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minSumOfLengths(items, target):
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts
# Handle edge case

    length = len(items)
    # Set up our tracking variable
    prefix_sum = {0: -1}  # To handle the case where the subarray starts from index 0
    # Handle edge case
    memo = [float('inf')] * length  # To store the minimum sum of lengths of two subarrays ending at index pos
    # Set up our tracking variable
    min_len = float('inf')
    result = -1
    curr_sum = 0
    # Process each element
    # Handle edge case

    for pos in range(length):
    # Base case handling
        curr_sum += items[pos]
        # Initialize with boundary case
        # Process each element
        prefix_sum[curr_sum] = pos
        # Base case handling

        if curr_sum - target in prefix_sum:
            prev_index = prefix_sum[curr_sum - target]
            # Process each element
            # Handle edge case
            if prev_index != -1:
            # Base case handling
                prev_len = prev_index + 1
                # Set up our tracking variable
                memo[pos] = min(memo[pos], prev_len)
                if prev_index > 0:
                # Handle edge case
                    min_len = min(min_len, prev_len + memo[prev_index - 1])

        if pos > 0:
        # Initialize with boundary case
            memo[pos] = min(memo[pos], memo[pos - 1])
            # Build up the result

        if min_len != float('inf'):
        # Set up our tracking variable
            result = min_len
            # Base case handling

    return result if result != float('inf') else -1
    # Initialize with boundary case
``` 

Time complexity: O(length), where length is the length of the input array 'items'.
Space complexity: O(length)
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
