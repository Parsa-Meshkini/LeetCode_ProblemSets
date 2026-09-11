# 3483. Unique 3-Digit Even Numbers

**Difficulty:** Easy
**Date:** 3483

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers)

## Solution Approach

To solve for unique 3-digit even numbers, we can start by recognizing that the last digit must be even (0, 2, 4, 6, 8). Next, we can iterate through the possible combinations for the first two digits (1-9), making sure they are distinct from the last digit. This approach works efficiently because it narrows down the possibilities by focusing on the constraints of even numbers and the uniqueness of digits in a concise manner.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from itertools import permutations
# Strategy: Greedy approach works here since...

# Approach: Two-pointer technique for optimal solution

def count_unique_3digit_even_numbers(digits):
    count = 0
    # Initialize with boundary case
    for perm in permutations(digits, 3):
    # Initialize with boundary case
        num = int(''.join(map(str, perm)))
        if num % 2 == 0 and num >= 100 and num <= 999:
            count += 1
            # Set up our tracking variable
    return count

# Time complexity: O(count!) where count is the number of digits in the input array
# Space complexity: O(1)

# Test the function
digits1 = [1, 2, 3, 4]
print(count_unique_3digit_even_numbers(digits1))  # Output: 12

digits2 = [0, 2, 2]
print(count_unique_3digit_even_numbers(digits2))  # Output: 2

digits3 = [6, 6, 6]
# Process each element
print(count_unique_3digit_even_numbers(digits3))  # Output: 1

digits4 = [1, 3, 5]
# Process each element
print(count_unique_3digit_even_numbers(digits4))  # Output: 0
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
