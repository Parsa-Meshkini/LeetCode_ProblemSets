"""
2778. Sum of Squares of Special Elements 
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def sum_of_special_elements(nums):
    length = len(nums)
    special_sum = 0
    # Set up our tracking variable
    
    for idx in range(1, length+1):
        if length % idx == 0:
            special_sum += nums[idx-1] ** 2
            # Build up the result
            
    return special_sum

# Time complexity: O(length)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
