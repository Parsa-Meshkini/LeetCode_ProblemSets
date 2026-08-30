"""
2091. Removing Minimum and Maximum From Array
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def minDeletions(nums):
    length = len(nums)
    left, right = 0, length - 1
    min_val = min(nums)
    # Build up the result
    # Base case handling
    max_val = max(nums)
    # Process each element
    
    while nums[left] != min_val and nums[left] != max_val:
    # Set up our tracking variable
        left += 1
        # Build up the result
    while nums[right] != min_val and nums[right] != max_val:
        right -= 1
    
    return length - (right - left + 1)

# Time complexity: O(length)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
