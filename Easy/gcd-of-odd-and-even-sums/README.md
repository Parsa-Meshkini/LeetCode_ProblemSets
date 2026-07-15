# 3658. GCD of Odd and Even Sums

**Difficulty:** Easy
**Date:** 3658

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums)

## Solution Approach

To solve "GCD of Odd and Even Sums," we can calculate the sum of the odd-indexed elements and the sum of the even-indexed elements separately. The key insight is that the GCD of these two sums is equal to the GCD of the difference between them and the smaller of the two sums. This approach works efficiently because it leverages the properties of GCD and reduces the problem to a simpler calculation.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
import math
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

def gcdOfSumOddAndEven(count):
    sumOdd = count ** 2
    sumEven = count * (count + 1)
    # Handle edge case
    return math.gcd(sumOdd, sumEven)

# Time complexity: O(1)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
