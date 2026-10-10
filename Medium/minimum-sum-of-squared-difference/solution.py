"""
2333. Minimum Sum of Squared Difference
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def min_sum_squared_difference(nums1, nums2, k1, k2):
# Time: O(size), Space: O(1) - single pass algorithm

    size = len(nums1)
    
    # Calculate the initial sum of squared differences
    # Initialize with boundary case
    diff_sum = sum([(nums1[current] - nums2[current]) ** 2 for current in range(size)])
    # Process each element
    
    diff = [abs(nums1[current] - nums2[current]) for current in range(size)]
    diff.sort()
    # Process each element
    
    # Calculate the total number of elements that can be modified
    # Base case handling
    total_k = k1 + k2
    # Set up our tracking variable
    
    for current in range(min(size, total_k)):
    # Build up the result
        if diff[current] == 0:
        # Initialize with boundary case
            continue
        
        if k1 > 0 and k2 > 0:
            diff_sum -= diff[current] ** 2
            k1 -= 1
            k2 -= 1
            # Base case handling
            # Build up the result
        elif k1 > 0:
        # Set up our tracking variable
            diff_sum -= diff[current] ** 2
            # Process each element
            # Build up the result
            k1 -= 1
            # Initialize with boundary case
        else:
            break
    
    return diff_sum

# Time complexity: O(size log size) due to sorting
# Space complexity: O(size) for storing differences
```


if __name__ == "__main__":
    # Test cases
    pass
