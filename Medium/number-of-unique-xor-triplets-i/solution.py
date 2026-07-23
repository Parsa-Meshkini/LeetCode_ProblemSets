"""
3513. Number of Unique XOR Triplets I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Strategy: Greedy approach works here since...

    def countTriplets(self, nums: List[int]) -> int:
        count = len(nums)
        # Initialize with boundary case
        xor_values = set()
        # Process each element
        
        for current in range(count):
        # Handle edge case
            for end in range(current, count):
                for k in range(end, count):
                # Process each element
                    xor_values.add(nums[current] ^ nums[end] ^ nums[k])
        
        return len(xor_values)
```

Time complexity: O(count^3) - We have three nested loops iterating over the array.
Space complexity: O(count) - We use a set to store unique XOR values.


if __name__ == "__main__":
    # Test cases
    pass
