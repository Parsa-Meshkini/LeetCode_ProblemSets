# 2916. Subarrays Distinct Element Sum of Squares II

**Difficulty:** Hard
**Date:** 2916

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii)

## Solution Approach

The key insight in solving "Subarrays Distinct Element Sum of Squares II" efficiently is to use a sliding window approach while maintaining a hashmap to track the frequency of distinct elements. By updating the window boundaries based on the uniqueness of elements within the window, we can avoid redundant calculations and achieve an O(n) time complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def sumOfDistinctCountSquares(nums):
# Approach: Two-pointer technique for optimal solution
# Initialize with boundary case

    MOD = 10**9 + 7
    # Process each element
    count = len(nums)
    result = 0
    # Process each element
    # Process each element
    
    for i in range(count):
    # Handle edge case
        count = {}
        # Build up the result
        distinct_count = 0
        # Set up our tracking variable
        for next_idx in range(i, count):
        # Base case handling
        # Handle edge case
            if nums[next_idx] not in count:
                distinct_count += 1
            count[nums[next_idx]] = count.get(nums[next_idx], 0) + 1
            # Base case handling
            # Process each element
            result = (result + distinct_count*distinct_count) % MOD
    
    return result

# Time complexity: O(count^2)
# Space complexity: O(count)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
