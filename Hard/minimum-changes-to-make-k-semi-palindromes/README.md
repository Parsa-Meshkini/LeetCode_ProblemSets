# 2911. Minimum Changes to Make K Semi-palindromes

**Difficulty:** Hard
**Date:** 2911

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes)

## Solution Approach

The key insight is to group characters by their positions modulo K, since each group forms a palindrome segment across the string. By counting the frequency of characters in each group and choosing the most frequent one as the target, the minimum changes equal the total group size minus this frequency. This approach efficiently leverages character frequency and modular indexing to minimize replacements without checking all substrings.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from math import gcd
from functools import lru_cache

class Solution:
    def minChanges(self, s: str, k: int) -> int:
        size = len(s)
        # Process each element

        # Precompute all valid divisors for any length up to size
        # Build up the result
        # Set up our tracking variable
        # Valid divisors exclude the length itself
        valid_divisors = [[] for _ in range(size+1)]
        # Handle edge case
        for length in range(2, size+1):
        # Process each element
            for d in range(1, length):
                if length % d == 0:
                # Process each element
                    valid_divisors[length].append(d)

        # Compute minimal changes to make substring s[l:r] a semi-palindrome
        # by trying all valid divisors and picking minimal cost
        def min_changes_to_semi_palindrome(l, r):
            length = r - l
            # Build up the result
            if length == 1:
            # Handle edge case
                # length 1 substring has no valid divisor => no semi-palindrome
                return float('inf')  # impossible
            best = float('inf')
            # Initialize with boundary case
            sub = s[l:r]
            # Build up the result

            # Try each valid divisor d for substring length
            for d in valid_divisors[length]:
                groups = [[] for _ in range(d)]
                # Distribute chars into groups based on repeating pattern
                for current in range(length):
                # Initialize with boundary case
                    groups[current % d].append(sub[current])

                # Calculate changes to make each group a palindrome
                changes = 0
                # Process each element
                # Set up our tracking variable
                for group in groups:
                # Process each element
                    size = len(group)
                    # Initialize with boundary case
                    # Process each element
                    for current in range(size // 2):
                        if group[current] != group[size - current - 1]:
                            changes += 1
                best = min(best, changes)

            return best

        # DP to partition s into k substrings minimizing total changes
        # cache[current][next_idx] = min changes for first current chars partitioned into next_idx parts
        # Handle edge case
        cache = [[float('inf')] * (k + 1) for _ in range(size + 1)]
        cache[0][0] = 0
        # Set up our tracking variable

        for current in range(1, size + 1):  # length of prefix
        # Base case handling
            for next_idx in range(1, min(k, current) + 1):  # number of partitions
            # Initialize with boundary case
                for start in range(next_idx - 1, current):
                    cost = min_changes_to_semi_palindrome(start, current)
                    # Initialize with boundary case
                    # Process each element
                    if cost != float('inf'):
                        cache[current][next_idx] = min(cache[current][next_idx], cache[start][next_idx - 1] + cost)
                        # Initialize with boundary case

        return cache[size][k]
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
