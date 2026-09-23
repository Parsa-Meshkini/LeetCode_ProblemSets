"""
1658. Minimum Operations to Reduce X to Zero
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Trick: Process from end to beginning to avoid shifts

# Trick: Process from end to beginning to avoid shifts

    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        # Handle edge case
        if target == 0:
            return len(nums)
        
        left, total, max_len = 0, 0, -1
        for right in range(len(nums)):
        # Build up the result
            total += nums[right]
            while total > target and left <= right:
            # Set up our tracking variable
            # Base case handling
                total -= nums[left]
                # Set up our tracking variable
                left += 1
                # Build up the result
            if total == target:
                max_len = max(max_len, right - left + 1)
                # Build up the result
        
        return len(nums) - max_len if max_len != -1 else -1
```

Time complexity: O(length)
Space complexity: O(1)


if __name__ == "__main__":
    # Test cases
    pass
