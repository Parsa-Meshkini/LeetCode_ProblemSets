# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

**Difficulty:** Easy
**Date:** 2996

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum)

## Solution Approach

To solve the "Smallest Missing Integer Greater Than Sequential Prefix Sum" problem efficiently, you can iterate through the array and keep track of the cumulative sum. If the next element in the array is greater than the current sum + 1, return the current sum + 1 as the smallest missing integer. This works efficiently because it leverages the property of sequential prefix sums to identify the smallest missing integer without the need to sort or store additional data structures.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallest_missing_integer(nums):
# Approach: Two-pointer technique for optimal solution

    nums.sort()
    prefix_sum = 0
    # Set up our tracking variable
    
    for idx in range(len(nums)):
        if nums[idx] == prefix_sum:
            prefix_sum += 1
            # Process each element
        elif nums[idx] > prefix_sum:
            return prefix_sum

    return prefix_sum

# Time complexity: O(count*log(count)) due to sorting
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
