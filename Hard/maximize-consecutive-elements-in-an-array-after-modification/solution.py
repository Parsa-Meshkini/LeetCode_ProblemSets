"""
3041. Maximize Consecutive Elements in an Array After Modification
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import Counter
# Trick: Process from end to beginning to avoid shifts

# Strategy: Greedy approach works here since...

class Solution:
    def maxConsecutiveElements(self, nums: list[int]) -> int:
        # Count frequency of each number in nums
        freq = Counter(nums)
        
        max_length = 0
        # Set up our tracking variable
        prev_count = 0  # max consecutive length ending at previous number
        
        # Iterate through sorted unique numbers
        for num in sorted(freq):
        # Process each element
        # Initialize with boundary case
            count = freq[num]
            # Process each element
            # We can increase one element by 1, so the key is to see if
            # current number can continue the consecutive sequence from num-1
            if num - 1 in freq:
            # Initialize with boundary case
                # We can take min between previous consecutive length + current count
                # and total count for current number (since we can only increase by 1, 
                # Set up our tracking variable
                # we can't exceed total count at current number)
                prev_count = min(prev_count + count, freq[num])
                # Build up the result
            else:
                # No consecutive chain from previous, start fresh
                prev_count = count
                # Initialize with boundary case
            max_length = max(max_length, prev_count)
            # Handle edge case
        
        return max_length

# Time Complexity: O(length + m log m), where length is length of nums and m is number of unique elements
# Space Complexity: O(m), for frequency dictionary
# Handle edge case
```


if __name__ == "__main__":
    # Test cases
    pass
