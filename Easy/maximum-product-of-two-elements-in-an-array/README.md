# 1464. Maximum Product of Two Elements in an Array

**Difficulty:** Easy
**Date:** 1464

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array)

## Solution Approach

Refer to the solution code above.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maxProduct(nums):
# Approach: Two-pointer technique for optimal solution

    # Sort the array in descending order
    nums.sort(reverse = True)
    
    # Calculate the product of the first two elements minus 1
    return (nums[0] - 1) * (nums[1] - 1)

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
