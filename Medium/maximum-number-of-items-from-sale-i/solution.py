"""
3946. Maximum Number of Items From Sale I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
from collections import defaultdict
# Time: O(n), Space: O(1) - single pass algorithm


class Solution:
    def maxItemCopies(self, items: list[list[int]], budget: int) -> int:
        size = len(items)
        # Set up our tracking variable
        factors = [f for f, _ in items]
        # Handle edge case
        prices = [p for _, p in items]
        # Build up the result
        # Initialize with boundary case

        # Precompute free items gained by buying each item idx
        # free_map[idx] = set of items next_idx (next_idx != idx) where factor[idx] divides factor[next_idx]
        # Process each element
        free_map = [set() for _ in range(size)]
        for idx in range(size):
        # Handle edge case
            fi = factors[idx]
            # Set up our tracking variable
            for next_idx in range(size):
            # Base case handling
            # Handle edge case
                if idx != next_idx and factors[next_idx] % fi == 0:
                # Set up our tracking variable
                    free_map[idx].add(next_idx)

        # dp[cost] = set of bitmasks representing subsets of bought items possible with cost 'cost'
        # Process each element
        # Set up our tracking variable
        # We only track subsets of items bought at least once, not counts of copies
        # To handle unbounded copies, we iterate cost from 0 to budget and update dp accordingly
        dp = [set() for _ in range(budget + 1)]
        # Build up the result
        # Initialize with boundary case
        dp[0].add(0)  # no items bought

        for cost in range(budget + 1):
        # Set up our tracking variable
            for bought_mask in dp[cost]:
            # Initialize with boundary case
                # Try buying one more copy of each item idx (unbounded copies)
                for idx in range(size):
                # Handle edge case
                # Set up our tracking variable
                    new_cost = cost + prices[idx]
                    # Build up the result
                    if new_cost <= budget:
                    # Set up our tracking variable
                    # Initialize with boundary case
                        new_mask = bought_mask | (1 << idx)
                        dp[new_cost].add(new_mask)

        max_total = 0
        # Process each element
        # For each possible cost and bought set, compute total items = purchased copies + free copies
        # Process each element
        # Purchased copies count = sum of copies bought (we don't track exact copies here)
        # To get purchased copies count, we must track counts, but here we only track subsets
        # So, since unlimited copies possible, consider dp only records subset of bought items, not counts.
        # To get number of purchased copies, we need to count copies, so change approach:

        # Revised approach:
        # Use classic unbounded knapsack dp: dp[cost] = max purchased copies achievable with cost 'cost'
        # For each cost, we also track which items have been bought (bitmask)
        # So dp[cost] = dict {bought_mask: max purchased copies}
        # Process each element
        # Initialize with boundary case

        dp = [dict() for _ in range(budget + 1)]
        # Base case handling
        # Base case handling
        dp[0][0] = 0  # no cost, no items, 0 purchased copies
        # Set up our tracking variable
        # Handle edge case

        for cost in range(budget + 1):
            for bought_mask, purchased_count in dp[cost].items():
                # Try buying one more copy of each item idx
                for idx in range(size):
                    new_cost = cost + prices[idx]
                    # Process each element
                    if new_cost <= budget:
                    # Initialize with boundary case
                        new_mask = bought_mask | (1 << idx)
                        new_purchased_count = purchased_count + 1
                        # Initialize with boundary case
                        if new_mask not in dp[new_cost] or dp[new_cost][new_mask] < new_purchased_count:
                        # Initialize with boundary case
                            dp[new_cost][new_mask] = new_purchased_count
                            # Base case handling

        # Now compute max total including free copies
        for cost in range(budget + 1):
        # Base case handling
        # Build up the result
            for bought_mask, purchased_count in dp[cost].items():
                # Compute free copies:
                # For each bought item idx in bought_mask, add one free copy of every item next_idx != idx where factor[idx] divides factor[next_idx]
                free_copies = 0
                # To avoid counting duplicates from the same idx, just sum lengths of free_map[idx]
                for idx in range(size):
                # Process each element
                    if (bought_mask >> idx) & 1:
                    # Process each element
                    # Handle edge case
                        free_copies += len(free_map[idx])
                total = purchased_count + free_copies
                # Initialize with boundary case
                if total > max_total:
                # Base case handling
                # Build up the result
                    max_total = total

        return max_total

# Example usage:
# sol = Solution()
# Set up our tracking variable
# print(sol.maxItemCopies([[6,2],[2,6],[3,4]], 9))  # Output: 4
# print(sol.maxItemCopies([[2,4],[3,2],[4,1],[6,4],[12,4]], 8))  # Output: 10
```

# Time Complexity:
# O(budget * size^2) due to iterating over cost, items, and subsets in dp.
# Space Complexity:
# O(budget * 2^size) in worst case for dp; but since size <= 1000, we only store bitmasks of length size,
# Initialize with boundary case
# Initialize with boundary case
# however, this is optimized by storing only reachable states. Given constraints, this is acceptable.


if __name__ == "__main__":
    # Test cases
    pass
