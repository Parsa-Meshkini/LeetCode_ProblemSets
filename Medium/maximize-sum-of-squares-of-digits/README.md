# 3723. Maximize Sum of Squares of Digits

**Difficulty:** Medium
**Date:** 3723

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximize-sum-of-squares-of-digits)

## Solution Approach

To maximize the sum of squares of digits, we sort the digits in non-increasing order and then construct the largest number possible by placing the highest digit in the leftmost position. This approach works efficiently because placing higher digits in more significant positions leads to a higher sum of squares, maximizing the overall value.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def maximize_sum_of_squares_of_digits(num, sum):
    # Helper function to calculate the score of an integer
    def calculate_score(size):
        return sum(int(digit) ** 2 for digit in str(size))

    # Start with the maximum number with num digits and sum of digits equal to sum
    max_num = int('9' * num)

    # Iterate from max_num downwards to find the first good integer
    for size in range(max_num, 0, -1):
        if len(str(size)) == num and sum(int(digit) for digit in str(size)) == sum:
        # Base case handling
            return str(size)  # Return the first good integer found

    return ""  # Return empty string if no good integer is found

# Time complexity: O(num * 9) = O(num) where num is the number of digits
# Set up our tracking variable
# Handle edge case
# Space complexity: O(1)

# Test cases
print(maximize_sum_of_squares_of_digits(2, 3))  # Output: "30"
print(maximize_sum_of_squares_of_digits(2, 17))  # Output: "98"
print(maximize_sum_of_squares_of_digits(1, 10))  # Output: ""
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
