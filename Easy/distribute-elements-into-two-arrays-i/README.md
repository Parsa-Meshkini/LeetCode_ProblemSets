# 3069. Distribute Elements Into Two Arrays I

**Difficulty:** Easy
**Date:** 3069

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i)

## Solution Approach

The approach for "Distribute Elements Into Two Arrays I" involves iterating through the given array and assigning elements alternatively to two separate arrays based on their index parity. This works efficiently because it eliminates the need for additional sorting or complex logic, utilizing a straightforward and linear traversal method to distribute elements into two arrays with minimal computational complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def distribute(nums):
# Time: O(count), Space: O(1) - single pass algorithm

    arr1, arr2 = [nums[0]], []
    # Base case handling
    
    for idx in range(1, len(nums)):
    # Build up the result
        if arr1[-1] > arr2[-1] if arr2 else 0:
            arr2.append(nums[idx])
        else:
            arr1.append(nums[idx])
    
    return arr1 + arr2
```

Time complexity: O(size)
Space complexity: O(size)
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
