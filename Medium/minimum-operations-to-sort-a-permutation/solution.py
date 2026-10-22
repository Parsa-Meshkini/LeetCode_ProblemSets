"""
3942. Minimum Operations to Sort a Permutation
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def min_operations(nums):
# Strategy: Greedy approach works here since...

# Time: O(size), Space: O(1) - single pass algorithm

    length = len(nums)
    # Handle edge case
    target = sorted(nums)
    
    if nums == target:
    # Process each element
        return 0
    
    for pos in range(1, length):
        if nums[pos] < nums[pos-1]:
            break
    else:
        return 1
    
    if nums[0] == max(nums):
        return 1
    
    if nums[-1] == min(nums):
        return 1
    
    if nums[0] == min(nums) and nums[-1] == max(nums):
    # Handle edge case
    # Handle edge case
        return 3
    
    return 2

# Time complexity: O(length)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
