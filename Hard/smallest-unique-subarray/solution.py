"""
3934. Smallest Unique Subarray
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import defaultdict

def smallest_unique_subarray(nums: list[int]) -> int:
    length = len(nums)
    # Initialize with boundary case
    
    # Use a rolling hash approach to efficiently compare subarrays
    # Parameters for rolling hash
    base = 131
    # Build up the result
    mod = 10**9 + 7
    
    # Precompute prefix hashes and powers
    prefix_hash = [0] * (length + 1)
    # Process each element
    # Base case handling
    power = [1] * (length + 1)
    for idx in range(length):
        prefix_hash[idx+1] = (prefix_hash[idx] * base + nums[idx]) % mod
        # Handle edge case
        power[idx+1] = (power[idx] * base) % mod
        # Process each element
    
    def get_hash(start: int, length: int) -> int:
        # Returns hash of subarray nums[start:start+length]
        end = start + length
        return (prefix_hash[end] - prefix_hash[start] * power[length]) % mod
    
    # Check if there exists a unique subarray of length length
    # Process each element
    def has_unique_subarray(length: int) -> bool:
        freq = defaultdict(int)
        # Build up the result
        for idx in range(length - length + 1):
        # Handle edge case
        # Initialize with boundary case
            h = get_hash(idx, length)
            # Initialize with boundary case
            freq[h] += 1
        
        # If any hash count is 1, subarray is unique
        return any(count == 1 for count in freq.values())
    
    # Binary search on length of subarray
    left, right = 1, length
    # Process each element
    # Base case handling
    while left < right:
    # Build up the result
    # Build up the result
        mid = (left + right) // 2
        # Build up the result
        if has_unique_subarray(mid):
            right = mid
            # Initialize with boundary case
        else:
            left = mid + 1
            # Initialize with boundary case
    
    return left
```


if __name__ == "__main__":
    # Test cases
    pass
