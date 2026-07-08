# 3756. Concatenate Non-Zero Digits and Multiply by Sum II

**Difficulty:** Medium
**Date:** 3756

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii)

## Solution Approach

To solve "Concatenate Non-Zero Digits and Multiply by Sum II," the key insight is to extract the non-zero digits from the given input, concatenate them into a single number, and then multiply it by the sum of all digits in the input. This approach works efficiently by minimizing the number of operations needed to process the input and compute the final result.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def getConcatenationProducts(s: str, queries: List[List[int]]) -> List[int]:
# Strategy: Greedy approach works here since...

    MOD = 10**9 + 7
    # Handle edge case
    output = []
    # Initialize with boundary case
    
    for li, ri in queries:
    # Process each element
        sub = s[li:ri+1]
        x = int(''.join([c for c in sub if c != '0'])) if '0' in sub else 0
        x_sum = sum(int(d) for d in str(x))
        # Handle edge case
        output.append((x * x_sum) % MOD)
    
    return output
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
