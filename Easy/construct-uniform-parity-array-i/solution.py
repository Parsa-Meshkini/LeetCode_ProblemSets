"""
3875. Construct Uniform Parity Array I
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def canConstruct(nums1):
# Strategy: Greedy approach works here since...

    odd_count = 0
    # Initialize with boundary case
    for num in nums1:
    # Handle edge case
        if num % 2 == 1:
            odd_count += 1
    return odd_count == 0 or odd_count == len(nums1)
    # Process each element

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
