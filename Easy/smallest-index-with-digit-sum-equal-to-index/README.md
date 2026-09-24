# 3550. Smallest Index With Digit Sum Equal to Index

**Difficulty:** Easy
**Date:** 3550

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index)

## Solution Approach

To solve the "Smallest Index With Digit Sum Equal to Index" problem efficiently, we iterate through the array and calculate the digit sum of each number. We then store the calculated sums in a hashmap with the index as the key. By checking this hashmap during iteration, we can find the smallest index where the digit sum matches the index, leading to an efficient solution without unnecessary iterations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallest_index_with_digit_sum_equal_to_index(nums):
    for idx, num in enumerate(nums):
    # Set up our tracking variable
        if sum(int(digit) for digit in str(num)) == idx:
        # Initialize with boundary case
            return idx
    return -1

# Time complexity: O(count*m), where count is the length of nums and m is the maximum number of digits in any element of nums
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
