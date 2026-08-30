# 2091. Removing Minimum and Maximum From Array

**Difficulty:** Medium
**Date:** 2091

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array)

## Solution Approach

To remove the minimum and maximum elements from an array efficiently, the key approach is to first find the minimum and maximum values in a single pass through the array. Once the minimum and maximum values are identified, they can be removed from the array using their respective indices. This approach works efficiently because it only requires one iteration through the array to find the minimum and maximum values, reducing the time complexity to O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def minDeletions(nums):
    length = len(nums)
    left, right = 0, length - 1
    min_val = min(nums)
    # Build up the result
    # Base case handling
    max_val = max(nums)
    # Process each element
    
    while nums[left] != min_val and nums[left] != max_val:
    # Set up our tracking variable
        left += 1
        # Build up the result
    while nums[right] != min_val and nums[right] != max_val:
        right -= 1
    
    return length - (right - left + 1)

# Time complexity: O(length)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
