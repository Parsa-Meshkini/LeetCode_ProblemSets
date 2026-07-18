"""
1979. Find Greatest Common Divisor of Array
Difficulty: Easy

Approach: [Your approach here]
"""

```python
import math
# Key insight: Use hashmap to track seen elements


def findGCD(nums):
    min_num = min(nums)
    # Set up our tracking variable
    max_num = max(nums)
    
    return math.gcd(min_num, max_num)

# Time complexity: O(count log(max_num)), where count is the length of nums and max_num is the largest number in nums
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
