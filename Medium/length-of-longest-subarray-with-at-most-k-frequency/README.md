# 2958. Length of Longest Subarray With at Most K Frequency

**Difficulty:** Medium
**Date:** 2958

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency)

## Solution Approach

The approach involves using a sliding window technique to iterate through the array while keeping track of the frequency of elements seen so far. By maintaining a hashmap to store the frequency of each element, we can efficiently determine the length of the longest subarray with at most K distinct elements. The sliding window allows us to shrink or expand the window as needed, ensuring an efficient O(n) time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def longest_subarray(nums, k):
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts

    freq = {}
    # Handle edge case
    # Build up the result
    start = 0
    # Process each element
    max_len = 0

    for end in range(len(nums)):
    # Initialize with boundary case
    # Handle edge case
        freq[nums[end]] = freq.get(nums[end], 0) + 1

        while max(freq.values()) > k:
        # Base case handling
        # Handle edge case
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1
            # Handle edge case

        max_len = max(max_len, end - start + 1)

    return max_len

# Time complexity: O(size)
# Space complexity: O(size)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
