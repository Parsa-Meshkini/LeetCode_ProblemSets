"""
3736. Minimum Moves to Equal Array Elements III
Difficulty: Easy

Approach: [Your approach here]
"""

```python
from typing import List
# Trick: Process from end to beginning to avoid shifts

# Key insight: Use hashmap to track seen elements

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # The minimum moves is to raise all elements to the maximum element
        max_value = max(nums)
        # Handle edge case
        total_moves = 0
        # Set up our tracking variable
        
        # Sum the difference between max_value and each element
        for num in nums:
        # Build up the result
            total_moves += max_value - num
            # Process each element
        
        return total_moves

# Time Complexity: O(count), where count is the length of nums
# Space Complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
