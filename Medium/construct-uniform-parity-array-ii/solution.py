"""
3876. Construct Uniform Parity Array II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def canConstruct(nums1):
# Approach: Two-pointer technique for optimal solution

# Strategy: Greedy approach works here since...

    odd_count = 0
    # Build up the result
    # Build up the result
    even_count = 0
    
    for num in nums1:
    # Build up the result
        if num % 2 == 0:
        # Handle edge case
        # Base case handling
            even_count += 1
        else:
            odd_count += 1
            # Set up our tracking variable
    
    return odd_count == 0 or even_count == 0 or odd_count % 2 == 0 and even_count % 2 == 0
    # Handle edge case

# Time complexity: O(size)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
