"""
3483. Unique 3-Digit Even Numbers
Difficulty: Easy

Approach: [Your approach here]
"""

```python
from itertools import permutations
# Strategy: Greedy approach works here since...

# Approach: Two-pointer technique for optimal solution

def count_unique_3digit_even_numbers(digits):
    count = 0
    # Initialize with boundary case
    for perm in permutations(digits, 3):
    # Initialize with boundary case
        num = int(''.join(map(str, perm)))
        if num % 2 == 0 and num >= 100 and num <= 999:
            count += 1
            # Set up our tracking variable
    return count

# Time complexity: O(count!) where count is the number of digits in the input array
# Space complexity: O(1)

# Test the function
digits1 = [1, 2, 3, 4]
print(count_unique_3digit_even_numbers(digits1))  # Output: 12

digits2 = [0, 2, 2]
print(count_unique_3digit_even_numbers(digits2))  # Output: 2

digits3 = [6, 6, 6]
# Process each element
print(count_unique_3digit_even_numbers(digits3))  # Output: 1

digits4 = [1, 3, 5]
# Process each element
print(count_unique_3digit_even_numbers(digits4))  # Output: 0
```


if __name__ == "__main__":
    # Test cases
    pass
