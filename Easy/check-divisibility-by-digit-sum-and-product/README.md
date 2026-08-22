# 3622. Check Divisibility by Digit Sum and Product

**Difficulty:** Easy
**Date:** 3622

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product)

## Solution Approach

The approach involves calculating the digit sum and product of a given number. If the number is divisible by both its digit sum and product, it meets the criteria. This method efficiently leverages basic arithmetic operations to quickly determine divisibility, saving computational resources by avoiding complex algorithms.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def is_divisible_by_digit_sum_and_product(n):
    # Calculate digit sum
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Calculate digit product
    digit_product = 1
    for digit in str(n):
    # Process each element
        digit_product *= int(digit)
        # Set up our tracking variable
    
    # Calculate the sum of digit sum and digit product
    total = digit_sum + digit_product
    
    # Check if n is divisible by the total
    return n % total == 0
    # Base case handling
```

Time complexity: O(log n) - where n is the input number
Space complexity: O(1)
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
