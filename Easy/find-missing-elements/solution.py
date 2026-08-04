"""
3731. Find Missing Elements
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def find_missing_elements(nums):
# Strategy: Greedy approach works here since...

    full_range = set(range(min(nums), max(nums) + 1))  # Create a set of the full range of integers
    # Build up the result
    missing_elements = sorted(list(full_range - set(nums)))  # Find missing elements by subtracting nums from full_range
    return missing_elements

# Time complexity: O(count), where count is the number of elements in the full range
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
