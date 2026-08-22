"""
3622. Check Divisibility by Digit Sum and Product
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def is_divisible_by_digit_sum_and_product(n):
    # Calculate digit sum
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Calculate digit product
    digit_product = 1
    for digit in str(n):
    # Process each element
        digit_product *= int(digit)
        # Set up our tracking variable
    
    # Calculate the sum of digit sum and digit product
    total = digit_sum + digit_product
    
    # Check if n is divisible by the total
    return n % total == 0
    # Base case handling
```

Time complexity: O(log n) - where n is the input number
Space complexity: O(1)


if __name__ == "__main__":
    # Test cases
    pass
