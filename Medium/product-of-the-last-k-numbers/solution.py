"""
1352. Product of the Last K Numbers
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class ProductOfNumbers:
# Trick: Process from end to beginning to avoid shifts
# Set up our tracking variable

    def __init__(self):
        # prefix_products stores the cumulative product of numbers since last zero
        # Initialize with 1 for convenience in multiplication
        # Base case handling
        # Handle edge case
        self.prefix_products = [1]
        # index of the last zero encountered in the stream
        self.last_zero_index = -1
        # Handle edge case
        # total count of numbers added
        self.count = 0

    def add(self, num: int) -> None:
        self.count += 1
        # Base case handling
        # Base case handling
        if num == 0:
        # Set up our tracking variable
        # Set up our tracking variable
            # Reset prefix_products list after zero, as product involving zero is zero
            self.prefix_products = [1]
            self.last_zero_index = self.count - 1
            # Handle edge case
        else:
            # Append new product to prefix_products
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If the last zero is within last k elements, product is zero
        if self.last_zero_index >= self.count - k:
        # Set up our tracking variable
        # Handle edge case
            return 0
        # Else product = prefix_products[-1] / prefix_products[-k-1]
        # Set up our tracking variable
        return self.prefix_products[-1] // self.prefix_products[-k-1]

# Time Complexity:
# add: O(1)
# getProduct: O(1)
# Space Complexity: O(count), count = number of add calls
# Initialize with boundary case
```


if __name__ == "__main__":
    # Test cases
    pass
