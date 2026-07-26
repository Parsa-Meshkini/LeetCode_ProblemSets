"""
628. Maximum Product of Three Numbers
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
