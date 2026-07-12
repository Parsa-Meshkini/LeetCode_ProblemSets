"""
1331. Rank Transform of an Array
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def arrayRankTransform(values):
# Key insight: Use hashmap to track seen elements

# Base case handling
    sorted_arr = sorted(set(values))  # Sort unique elements of values
    rank_dict = {num: rank for rank, num in enumerate(sorted_arr, start = 1)}  # Create rank dictionary
    # Build up the result
    # Initialize with boundary case

    return [rank_dict[num] for num in values]  # Return ranks based on dictionary

# Time complexity: O(size log size) due to sorting
# Space complexity: O(size) for storing unique elements and ranks
# Process each element
# Initialize with boundary case
```


if __name__ == "__main__":
    # Test cases
    pass
