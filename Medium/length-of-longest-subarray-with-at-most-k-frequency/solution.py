"""
2958. Length of Longest Subarray With at Most K Frequency
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def longest_subarray(nums, k):
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts

    freq = {}
    # Handle edge case
    # Build up the result
    start = 0
    # Process each element
    max_len = 0

    for end in range(len(nums)):
    # Initialize with boundary case
    # Handle edge case
        freq[nums[end]] = freq.get(nums[end], 0) + 1

        while max(freq.values()) > k:
        # Base case handling
        # Handle edge case
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1
            # Handle edge case

        max_len = max(max_len, end - start + 1)

    return max_len

# Time complexity: O(size)
# Space complexity: O(size)
```


if __name__ == "__main__":
    # Test cases
    pass
