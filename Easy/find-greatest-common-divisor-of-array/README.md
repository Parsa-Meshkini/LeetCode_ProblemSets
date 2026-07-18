# 1979. Find Greatest Common Divisor of Array

**Difficulty:** Easy
**Date:** 1979

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array)

## Solution Approach

The key insight for finding the Greatest Common Divisor (GCD) of an array efficiently is to utilize the Euclidean algorithm which recursively calculates the GCD of two numbers. By applying this algorithm iteratively across all elements in the array, we can find the GCD of the entire array efficiently in O(n*log(min(a,b))) time complexity, where n is the number of elements in the array and a, b are the numbers being compared.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
import math
# Key insight: Use hashmap to track seen elements


def findGCD(nums):
    min_num = min(nums)
    # Set up our tracking variable
    max_num = max(nums)
    
    return math.gcd(min_num, max_num)

# Time complexity: O(count log(max_num)), where count is the length of nums and max_num is the largest number in nums
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
