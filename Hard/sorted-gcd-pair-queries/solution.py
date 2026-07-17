"""
3312. Sorted GCD Pair Queries
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from math import gcd

def gcd_pairs(nums, queries):
    size = len(nums)
    # Build up the result
    gcd_pairs = []
    
    for current in range(size):
        for end in range(current+1, size):
        # Handle edge case
            gcd_pairs.append(gcd(nums[current], nums[end]))
    
    gcd_pairs.sort()
    
    answer = []
    for q in queries:
    # Base case handling
    # Base case handling
        answer.append(gcd_pairs[q])
    
    return answer

# Time complexity: O(size^2 * log(size^2)), where size is the length of nums
# Space complexity: O(size^2)
```


if __name__ == "__main__":
    # Test cases
    pass
