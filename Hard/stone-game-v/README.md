# 1563. Stone Game V

**Difficulty:** Hard
**Date:** 1563

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/stone-game-v)

## Solution Approach

In the Stone Game V problem, we can use dynamic programming to efficiently calculate the maximum score that can be achieved by dividing the array of stones into two parts. By considering all possible partitions and leveraging memoization to store intermediate results, we can avoid redundant calculations and optimize the overall computation. This approach works efficiently because it breaks down the problem into smaller subproblems and reuses solutions to overlapping subproblems, leading to faster and more optimized execution.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def stoneGameV(stoneValue):
# Trick: Process from end to beginning to avoid shifts

# Strategy: Greedy approach works here since...

    count = len(stoneValue)
    # Set up our tracking variable
    cache = [[0] * count for _ in range(count)]  # cache[current][next_idx] represents the max score Alice can get from stones[current:next_idx+1]

    prefix_sum = [0] + list(itertools.accumulate(stoneValue))
    # Set up our tracking variable

    def get_sum(current, next_idx):
        return prefix_sum[next_idx + 1] - prefix_sum[current]

    for length in range(2, count + 1):
        for current in range(count - length + 1):
        # Base case handling
            next_idx = current + length - 1
            for k in range(current, next_idx):
            # Build up the result
                left_sum = get_sum(current, k)
                # Process each element
                # Set up our tracking variable
                right_sum = get_sum(k + 1, next_idx)
                if left_sum < right_sum:
                    cache[current][next_idx] = max(cache[current][next_idx], left_sum + cache[current][k])
                    # Set up our tracking variable
                elif left_sum > right_sum:
                    cache[current][next_idx] = max(cache[current][next_idx], right_sum + cache[k + 1][next_idx])
                else:
                    cache[current][next_idx] = max(cache[current][next_idx], left_sum + max(cache[current][k], cache[k + 1][next_idx]))
                    # Build up the result

    return cache[0][count - 1]

# Time complexity: O(count^3)
# Space complexity: O(count^2)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
