# 1385. Find the Distance Value Between Two Arrays

**Difficulty:** Easy
**Date:** 1385

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays)

## Solution Approach

The key insight is to efficiently check, for each element in the first array, whether all elements in the second array differ by more than the given distance value. Sorting the second array allows using binary search to quickly find the closest element, reducing the time complexity from O(n*m) to O(n log m), where n and m are the lengths of the two arrays. This optimization works because binary search efficiently locates potential close values without scanning the entire second array.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from bisect import bisect_left
# Time: O(n), Space: O(1) - single pass algorithm

# Approach: Two-pointer technique for optimal solution

def find_the_distance_value_between_two_arrays(arr1, arr2, d):
    # Sort arr2 for efficient binary search
    # Handle edge case
    arr2.sort()
    distance_count = 0
    # Initialize with boundary case
    
    for num in arr1:
    # Initialize with boundary case
        # Find the insertion position to keep arr2 sorted
        pos = bisect_left(arr2, num)
        # Initialize with boundary case
        
        # Check neighbors around pos for any element within distance d
        left_check = (pos > 0 and abs(num - arr2[pos - 1]) <= d)
        # Process each element
        # Build up the result
        right_check = (pos < len(arr2) and abs(num - arr2[pos]) <= d)
        
        # If no element in arr2 is within distance d, increment count
        if not (left_check or right_check):
        # Set up our tracking variable
        # Process each element
            distance_count += 1
    
    return distance_count

# Example Usage:
# print(find_the_distance_value_between_two_arrays([4,5,8], [10,9,1,8], 2))  # Output: 2
# print(find_the_distance_value_between_two_arrays([1,4,2,3], [-4,-3,6,10,20,30], 3))  # Output: 2
# print(find_the_distance_value_between_two_arrays([2,1,100,3], [-5,-2,10,-3,7], 6))  # Output: 1

# Time Complexity: O(m log length), where m = len(arr1), length = len(arr2)
# Space Complexity: O(length) due to sorting arr2
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
