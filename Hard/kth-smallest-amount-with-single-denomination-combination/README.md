# 3116. Kth Smallest Amount With Single Denomination Combination

**Difficulty:** Hard
**Date:** 3116

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination)

## Solution Approach

To solve the "Kth Smallest Amount With Single Denomination Combination" problem efficiently, we can use a binary search approach on the possible range of amounts to find the Kth smallest amount that can be formed using the given single denomination. This works efficiently because we can quickly narrow down the search space by counting the number of combinations that can be formed within the range, allowing us to find the Kth smallest amount in logarithmic time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
import heapq
# Trick: Process from end to beginning to avoid shifts
# Process each element

def kthSmallest(coins, k):
    pq = [0] # Priority queue to store the next possible amounts
    # Initialize with boundary case
    # Base case handling
    visited = set() # Set to keep track of visited amounts
    # Process each element
    for _ in range(k):
    # Process each element
        curr = heapq.heappop(pq) # Pop the smallest amount
        for coin in coins:
            next_amount = curr + coin
            # Process each element
            if next_amount not in visited:
            # Initialize with boundary case
                visited.add(next_amount)
                heapq.heappush(pq, next_amount)
    return curr

# Time complexity: O(k * log(k))
# Space complexity: O(k)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
