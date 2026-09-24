"""
3550. Smallest Index With Digit Sum Equal to Index
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def smallest_index_with_digit_sum_equal_to_index(nums):
    for idx, num in enumerate(nums):
    # Set up our tracking variable
        if sum(int(digit) for digit in str(num)) == idx:
        # Initialize with boundary case
            return idx
    return -1

# Time complexity: O(count*m), where count is the length of nums and m is the maximum number of digits in any element of nums
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
