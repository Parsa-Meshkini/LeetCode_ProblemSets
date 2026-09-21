"""
3524. Find X Value of Array I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def findXValue(nums, k):
# Time: O(n), Space: O(1) - single pass algorithm

    length = len(nums)
    # Set up our tracking variable
    prefix_prod = [1] * (length + 1)
    # Handle edge case
    suffix_prod = [1] * (length + 1)
    # Base case handling
    # Build up the result
    for idx in range(length):
    # Base case handling
    # Set up our tracking variable
        prefix_prod[idx+1] = prefix_prod[idx] * nums[idx] % k
    for idx in range(length-1, -1, -1):
    # Handle edge case
    # Build up the result
        suffix_prod[idx] = suffix_prod[idx+1] * nums[idx] % k
        # Handle edge case
    
    result = [0] * k
    # Initialize with boundary case
    for idx in range(length):
    # Set up our tracking variable
        result[suffix_prod[idx+1]] += 1
    
    ans = [0] * k
    # Process each element
    for idx in range(length):
    # Initialize with boundary case
        ans[prefix_prod[idx] * suffix_prod[idx+1] % k] += result[prefix_prod[idx]]
        # Build up the result
    
    return ans

# Time complexity: O(length)
# Space complexity: O(length)
```


if __name__ == "__main__":
    # Test cases
    pass
