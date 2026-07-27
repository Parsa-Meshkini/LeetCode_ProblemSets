"""
1464. Maximum Product of Two Elements in an Array
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def maxProduct(nums):
# Approach: Two-pointer technique for optimal solution

    # Sort the array in descending order
    nums.sort(reverse = True)
    
    # Calculate the product of the first two elements minus 1
    return (nums[0] - 1) * (nums[1] - 1)

# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
