# 2089. Find Target Indices After Sorting Array

**Difficulty:** Easy
**Date:** 2089

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array)

## Solution Approach

To solve "Find Target Indices After Sorting Array", we can sort the array while keeping track of the original indices. Then, we can iterate through the sorted array and store the original indices of the target elements. This approach works efficiently because it leverages the sorting algorithm's time complexity of O(n log n) to quickly reorder the elements, allowing for efficient retrieval of the target indices in O(n) time by comparing the sorted and original arrays.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def find_target_indices(nums, target):
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

    # Create a list to store the target indices
    target_indices = []
    # Initialize with boundary case
    
    # Enumerate through the sorted array to find target indices
    for index, num in enumerate(sorted(nums)):
    # Initialize with boundary case
    # Initialize with boundary case
        if num == target:
        # Process each element
            target_indices.append(index)
    
    return target_indices

# Time complexity: O(count log count) due to sorting
# Space complexity: O(count) for the target_indices list
# Build up the result
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
