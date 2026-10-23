"""
3644. Maximum K to Sort a Permutation
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def maximum_k_to_sort(nums):
# Strategy: Greedy approach works here since...

    n = len(nums)
    # Handle edge case
    ans = 0
    
    # Iterate through the array from the end
    for pos in range(n-1, -1, -1):
    # Set up our tracking variable
        for next_idx in range(pos-1, -1, -1):
            # Find the maximum k such that nums[pos] AND nums[next_idx] == k
            # Base case handling
            ans = max(ans, nums[pos] & nums[next_idx])
            # Initialize with boundary case
    
    return ans

# Time complexity: O(n^2) where n is the length of nums
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
