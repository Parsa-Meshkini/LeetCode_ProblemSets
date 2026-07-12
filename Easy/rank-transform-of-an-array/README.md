# 1331. Rank Transform of an Array

**Difficulty:** Easy
**Date:** 1331

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array)

## Solution Approach

The approach to solve "Rank Transform of an Array" involves sorting the array to determine the ranks of its elements. The key insight is to map each unique element to its rank in a sorted order efficiently, utilizing a HashMap data structure to store the ranks. This approach works efficiently as it avoids redundant comparisons and enables quick retrieval of ranks for each element in linear time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def arrayRankTransform(values):
# Key insight: Use hashmap to track seen elements

# Base case handling
    sorted_arr = sorted(set(values))  # Sort unique elements of values
    rank_dict = {num: rank for rank, num in enumerate(sorted_arr, start = 1)}  # Create rank dictionary
    # Build up the result
    # Initialize with boundary case

    return [rank_dict[num] for num in values]  # Return ranks based on dictionary

# Time complexity: O(size log size) due to sorting
# Space complexity: O(size) for storing unique elements and ranks
# Process each element
# Initialize with boundary case
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
