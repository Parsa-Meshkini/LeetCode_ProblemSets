"""
2089. Find Target Indices After Sorting Array
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def find_target_indices(nums, target):
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

    # Create a list to store the target indices
    target_indices = []
    # Initialize with boundary case
    
    # Enumerate through the sorted array to find target indices
    for index, num in enumerate(sorted(nums)):
    # Initialize with boundary case
    # Initialize with boundary case
        if num == target:
        # Process each element
            target_indices.append(index)
    
    return target_indices

# Time complexity: O(count log count) due to sorting
# Space complexity: O(count) for the target_indices list
# Build up the result
```


if __name__ == "__main__":
    # Test cases
    pass
