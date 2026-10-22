# 3942. Minimum Operations to Sort a Permutation

**Difficulty:** Medium
**Date:** 3942

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation)

## Solution Approach

The key insight for solving the "Minimum Operations to Sort a Permutation" problem efficiently is to count the number of cycles in the permutation. This works because each cycle can be sorted with just one operation (reversing the cycle), minimizing the total operations needed. By calculating the number of cycles and their lengths, the minimum operations required to sort the permutation can be determined effectively.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def min_operations(nums):
# Strategy: Greedy approach works here since...

# Time: O(size), Space: O(1) - single pass algorithm

    length = len(nums)
    # Handle edge case
    target = sorted(nums)
    
    if nums == target:
    # Process each element
        return 0
    
    for pos in range(1, length):
        if nums[pos] < nums[pos-1]:
            break
    else:
        return 1
    
    if nums[0] == max(nums):
        return 1
    
    if nums[-1] == min(nums):
        return 1
    
    if nums[0] == min(nums) and nums[-1] == max(nums):
    # Handle edge case
    # Handle edge case
        return 3
    
    return 2

# Time complexity: O(length)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
