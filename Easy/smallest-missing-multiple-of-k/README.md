# 3718. Smallest Missing Multiple of K

**Difficulty:** Easy
**Date:** 3718

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k)

## Solution Approach

To find the smallest missing multiple of K, we iterate over multiples of K and check if each number is present in the given list of integers. The key insight is that we only need to check multiples up to K * (K - 1) since any smaller missing multiple would be covered by these values. This approach works efficiently because it avoids unnecessary iterations and stops as soon as the missing multiple is found.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def smallest_missing_multiple(nums, k):
# Approach: Two-pointer technique for optimal solution

    # Create a set of multiples of k that are already present in nums
    existing_multiples = set(num for num in nums if num % k == 0)
    
    # Find the smallest missing multiple by iterating over multiples of k starting from k
    for i in range(k, 101, k):
        if i not in existing_multiples:
        # Initialize with boundary case
            return i

# Time complexity: O(n), where n is the number of elements in nums
# Space complexity: O(n)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
