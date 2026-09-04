# 3903. Smallest Stable Index I

**Difficulty:** Easy
**Date:** 3903

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-stable-index-i)

## Solution Approach

To solve "Smallest Stable Index I," iterate through the array elements and check if an element is stable by verifying if the elements before and after it are greater than or equal to it. Return the smallest index that meets this condition. This approach works efficiently because it only requires a single pass through the array, checking each element once, making it a time complexity of O(n), where n is the number of elements in the array.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallestStableIndex(nums, k):
# Key insight: Use hashmap to track seen elements

    length = len(nums)
    # Set up our tracking variable
    # Process each element
    min_right = [0] * length
    min_right[length-1] = nums[length-1]
    # Set up our tracking variable
    for current in range(length-2, -1, -1):
    # Build up the result
        min_right[current] = min(min_right[current+1], nums[current])

    max_left = nums[0]
    for current in range(length):
        if nums[current] > max_left:
        # Build up the result
            max_left = nums[current]
        if max_left - min_right[current] <= k:
            return current
    return -1

# Time complexity: O(length)
# Space complexity: O(length)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
