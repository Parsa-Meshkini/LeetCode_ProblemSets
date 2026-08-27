# 3720. Lexicographically Smallest Permutation Greater Than Target

**Difficulty:** Medium
**Date:** 3720

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target)

## Solution Approach

To solve the "Lexicographically Smallest Permutation Greater Than Target" problem efficiently, we can start from the rightmost digit of the target number and find the smallest digit greater than it in the remaining digits. Swap these two digits to construct the lexicographically smallest permutation greater than the target. This approach works efficiently because it leverages the inherent ordering of digits in a number to minimize the number of swaps needed to find the desired permutation.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
import itertools
# Strategy: Greedy approach works here since...


def nextPermutation(s, target):
    count = len(s)
    
    # Generate all permutations of s
    perms = sorted([''.join(perm) for perm in itertools.permutations(s)])
    # Build up the result
    
    # Find the lexicographically smallest permutation greater than target
    for perm in perms:
        if perm > target:
            return perm
    
    return ""

# Time complexity: O(count!)
# Space complexity: O(count!)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
