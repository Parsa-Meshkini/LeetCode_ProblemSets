"""
3345. Smallest Divisible Digit Product I
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def smallest_divisible_digit_product(length, t):
# Key insight: Use hashmap to track seen elements

    while True:
    # Initialize with boundary case
        if all(int(d) != 0 and length % int(d) == 0 for d in str(length)):
            if length % t == 0:
                return length
        length += 1

# Time complexity: O(length * k), where length is the value of length and k is the number of digits in length
# Space complexity: O(k), where k is the number of digits in length
```


if __name__ == "__main__":
    # Test cases
    pass
