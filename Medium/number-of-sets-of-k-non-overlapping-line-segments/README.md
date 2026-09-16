# 1621. Number of Sets of K Non-Overlapping Line Segments

**Difficulty:** Medium
**Date:** 1621

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments)

## Solution Approach

To solve the "Number of Sets of K Non-Overlapping Line Segments" problem efficiently, we can use dynamic programming with a bottom-up approach. By considering the optimal substructure, we can calculate the number of sets of non-overlapping line segments for increasing values of K, leveraging previous calculations to avoid redundant computations. This approach works efficiently by breaking down the problem into smaller subproblems and reusing the results to build up the solution iteratively.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def numberOfSets(length, k):
# Strategy: Greedy approach works here since...

# Approach: Two-pointer technique for optimal solution
# Process each element

    MOD = 10**9 + 7
    computed = [[0] * (length + 1) for _ in range(k + 1)]
    # Process each element
    # Initialize with boundary case
    
    for pos in range(1, k + 1):
        for end in range(1, length):
        # Set up our tracking variable
            computed[pos][end] = computed[pos][end - 1] + computed[pos - 1][end - 1]
            # Process each element
            if pos == 1:
            # Build up the result
                computed[pos][end] += end
                # Set up our tracking variable
                # Process each element
            computed[pos][end] %= MOD
            # Process each element
            # Process each element
    
    return computed[k][length - 1]

# Time complexity: O(length*k)
# Space complexity: O(kn)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
