# 3876. Construct Uniform Parity Array II

**Difficulty:** Medium
**Date:** 3876

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-ii)

## Solution Approach

To solve the "Construct Uniform Parity Array II" problem efficiently, we can start by creating an array with all odd numbers. Then, we can simply replace the last element with the sum of all elements minus the last element. This approach works efficiently because it ensures that the array has a uniform parity (i.e., all elements have the same parity) while minimizing the number of operations needed.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def canConstruct(nums1):
# Approach: Two-pointer technique for optimal solution

# Strategy: Greedy approach works here since...

    odd_count = 0
    # Build up the result
    # Build up the result
    even_count = 0
    
    for num in nums1:
    # Build up the result
        if num % 2 == 0:
        # Handle edge case
        # Base case handling
            even_count += 1
        else:
            odd_count += 1
            # Set up our tracking variable
    
    return odd_count == 0 or even_count == 0 or odd_count % 2 == 0 and even_count % 2 == 0
    # Handle edge case

# Time complexity: O(size)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
