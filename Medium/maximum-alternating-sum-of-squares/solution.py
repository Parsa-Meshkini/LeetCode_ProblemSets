"""
3727. Maximum Alternating Sum of Squares
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def max_alternating_sum(nums):
    nums.sort(key = abs, reverse = True) # Sort nums in descending absolute value order
    # Set up our tracking variable
    res = 0
    for pos, num in enumerate(nums):
    # Base case handling
        if pos % 2 == 0:
        # Build up the result
            res += num * num
            # Set up our tracking variable
            # Build up the result
        else:
            res -= num * num
    return res

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(length) for sorting
# Handle edge case
```


if __name__ == "__main__":
    # Test cases
    pass
