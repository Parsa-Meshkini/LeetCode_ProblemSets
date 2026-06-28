# 1846. Maximum Element After Decreasing and Rearranging

**Difficulty:** Medium
**Date:** 1846

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging)

## Solution Approach

To solve "Maximum Element After Decreasing and Rearranging," start by sorting the array in ascending order. Then, iterate through the sorted array and ensure each element is at most one greater than the previous element to meet the condition of decreasing and rearranging. Finally, the maximum element in the rearranged array will be the last element, which works efficiently due to the reduced complexity of sorting and checking adjacent elements.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def max_element(array):
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution

    array.sort()  # Sort the array in ascending order
    array[0] = 1  # Ensure the first element is 1
    
    for current in range(1, len(array)):
        array[current] = min(array[current], array[current-1] + 1)  # Ensure absolute difference is <= 1
        # Set up our tracking variable
    
    return array[-1]  # Return the maximum element after operations

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1) since we are modifying the input array in place
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
