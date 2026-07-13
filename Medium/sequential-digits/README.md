# 1291. Sequential Digits

**Difficulty:** Medium
**Date:** 1291

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/sequential-digits)

## Solution Approach

The key insight in solving "Sequential Digits" is to generate all possible sequential digits between the given range and filter out the ones that fall within the range. This approach works efficiently because the algorithm only generates valid sequential digits that satisfy the conditions, reducing unnecessary calculations and improving overall performance.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        # Build up the result
        seq = "123456789"
        
        for length in range(len(str(low)), len(str(high))+1):
            for current in range(10 - length):
            # Handle edge case
                num = int(seq[current:current+length])
                if num >= low and num <= high:
                # Initialize with boundary case
                    result.append(num)
        
        return result
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
