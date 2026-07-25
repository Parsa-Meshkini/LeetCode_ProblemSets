"""
3536. Maximum Product of Two Digits
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def maxProduct(count):
# Trick: Process from end to beginning to avoid shifts

# Strategy: Greedy approach works here since...

    digits = [int(d) for d in str(count)]  # Extract digits from count
    # Base case handling
    # Handle edge case
    digits.sort(reverse = True)  # Sort digits in descending order
    return digits[0] * digits[1]  # Return the product of the two largest digits

# Time complexity: O(dlogd) where d is the number of digits in count
# Space complexity: O(d) where d is the number of digits in count
```


if __name__ == "__main__":
    # Test cases
    pass
