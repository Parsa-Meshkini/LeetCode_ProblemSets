# 3536. Maximum Product of Two Digits

**Difficulty:** Easy
**Date:** 3536

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits)

## Solution Approach

To solve the "Maximum Product of Two Digits" problem, identify the two largest digits in the given number. Multiply these two digits to get the maximum product. This approach works efficiently because it involves a simple comparison to find the largest digits, making the solution straightforward and quick to implement.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maxProduct(count):
# Trick: Process from end to beginning to avoid shifts

# Strategy: Greedy approach works here since...

    digits = [int(d) for d in str(count)]  # Extract digits from count
    # Base case handling
    # Handle edge case
    digits.sort(reverse = True)  # Sort digits in descending order
    return digits[0] * digits[1]  # Return the product of the two largest digits

# Time complexity: O(dlogd) where d is the number of digits in count
# Space complexity: O(d) where d is the number of digits in count
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
