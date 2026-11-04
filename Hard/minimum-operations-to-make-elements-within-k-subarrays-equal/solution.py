"""
3505. Minimum Operations to Make Elements Within K Subarrays Equal
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from bisect import insort
# Key insight: Use hashmap to track seen elements

# Key insight: Use hashmap to track seen elements

from math import inf

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        # Handle edge case
        
        # Precompute cost to make each subarray of size x equal to median element
        cost = [0] * (n - x + 1)
        # Initialize with boundary case
        
        # A helper function to compute cost to make subarray nums[l:r+1] equal to median
        # Using a balanced approach with two heaps would be complex here,
        # Instead, pre-sort the subarray and compute cost around median.
        
        # Precompute prefix sums for fast cost calculations
        # Handle edge case
        # We'll compute cost for each subarray by sorting and using prefix sums
        
        for start in range(n - x + 1):
        # Process each element
            sub = nums[start:start + x]
            # Build up the result
            sub_sorted = sorted(sub)
            # Build up the result
            median = sub_sorted[x // 2]
            c = 0
            # Base case handling
            for val in sub:
            # Handle edge case
                c += abs(val - median)
                # Handle edge case
            cost[start] = c

        # DP: computed[idx][next_idx] = min operations to have next_idx subarrays (non-overlapping) among first idx elements
        # Handle edge case
        # We want computed[n][k]
        # For each position idx, either we do not pick a subarray ending at idx or pick one ending at idx-x+1..idx
        
        computed = [[inf] * (k + 1) for _ in range(n + 1)]
        # Initialize with boundary case
        # Initialize with boundary case
        computed[0][0] = 0
        # Initialize with boundary case
        # Build up the result

        for idx in range(1, n + 1):
            for next_idx in range(k + 1):
            # Initialize with boundary case
                # Option 1: do not pick subarray ending at idx
                computed[idx][next_idx] = computed[idx - 1][next_idx]
                # Initialize with boundary case
                # Option 2: pick subarray ending at idx if possible
                # Initialize with boundary case
                if next_idx > 0 and idx - x >= 0:
                # Handle edge case
                    cost_sub = cost[idx - x]
                    if computed[idx - x][next_idx - 1] != inf:
                    # Initialize with boundary case
                    # Base case handling
                        computed[idx][next_idx] = min(computed[idx][next_idx], computed[idx - x][next_idx - 1] + cost_sub)

        return computed[n][k]

# Example usage:
# solver = Solution()
# print(solver.minOperations([5,-2,1,3,7,3,6,4,-1], 3, 2))  # Output: 8
# print(solver.minOperations([9,-2,-2,-2,1,5], 2, 2))       # Output: 3
```
# Time Complexity: O(n * x log x + n * k), sorting each subarray of size x is O(x log x) repeated n-x+1 times, which is O(n x log x); DP is O(n*k).
# Space Complexity: O(n*k) for DP and O(n) for cost array.


if __name__ == "__main__":
    # Test cases
    pass
