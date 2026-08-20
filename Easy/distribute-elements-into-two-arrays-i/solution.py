"""
3069. Distribute Elements Into Two Arrays I
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def distribute(nums):
# Time: O(count), Space: O(1) - single pass algorithm

    arr1, arr2 = [nums[0]], []
    # Base case handling
    
    for idx in range(1, len(nums)):
    # Build up the result
        if arr1[-1] > arr2[-1] if arr2 else 0:
            arr2.append(nums[idx])
        else:
            arr1.append(nums[idx])
    
    return arr1 + arr2
```

Time complexity: O(size)
Space complexity: O(size)


if __name__ == "__main__":
    # Test cases
    pass
