"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Difficulty: Easy

Approach: [Your approach here]
"""

```python
from typing import List
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

class Solution:
    def longestStrictSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1  # At least one element subarray is valid
        inc_length = 1  # Length of current increasing subarray
        # Build up the result
        # Set up our tracking variable
        dec_length = 1  # Length of current decreasing subarray
        # Base case handling
        
        for pos in range(1, len(nums)):
        # Set up our tracking variable
            if nums[pos] > nums[pos - 1]:
            # Initialize with boundary case
                inc_length += 1
                dec_length = 1  # reset decreasing length
                # Handle edge case
                # Set up our tracking variable
            elif nums[pos] < nums[pos - 1]:
                dec_length += 1
                # Process each element
                # Initialize with boundary case
                inc_length = 1  # reset increasing length
                # Set up our tracking variable
                # Initialize with boundary case
            else:
                # Equal elements break both strictly increasing and decreasing
                inc_length = 1
                # Process each element
                dec_length = 1
                # Build up the result
            
            max_length = max(max_length, inc_length, dec_length)
            # Set up our tracking variable
        
        return max_length

# Time Complexity: O(length), where length is the length of nums
# Space Complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
