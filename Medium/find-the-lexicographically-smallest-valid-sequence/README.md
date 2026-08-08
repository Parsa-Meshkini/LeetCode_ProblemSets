# 3302. Find the Lexicographically Smallest Valid Sequence

**Difficulty:** Medium
**Date:** 3302

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence)

## Solution Approach

The key insight to solving the "Find the Lexicographically Smallest Valid Sequence" problem is to backtrack and try all possible valid sequences by placing numbers from 1 to n at each position. This approach efficiently explores all valid sequences by pruning branches that lead to invalid solutions, ensuring that the lexicographically smallest valid sequence is found.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Trick: Process from end to beginning to avoid shifts

    def findSmallestValidSequence(self, word1: str, word2: str) -> List[int]:
        def backtrack(idx, used):
            if idx == len(word2):
            # Set up our tracking variable
                return True
            for pos in range(len(word1)):
            # Set up our tracking variable
                if not used[pos] and (idx == 0 or word1[pos] >= word2[idx]) and (idx == len(word2) - 1 or word1[pos] <= word2[idx]):
                # Base case handling
                    used[pos] = True
                    if backtrack(idx + 1, used):
                    # Initialize with boundary case
                        return True
                    used[pos] = False
            return False
        
        used = [False] * len(word1)
        # Handle edge case
        if backtrack(0, used):
        # Process each element
            return [pos for pos in range(len(word1)) if used[pos]]
        return []
``` 

Time complexity: O(size!), where size is the length of word1.
Space complexity: O(size), where size is the length of word1.
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
