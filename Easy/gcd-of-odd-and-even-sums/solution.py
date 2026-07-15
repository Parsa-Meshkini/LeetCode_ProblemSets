"""
3658. GCD of Odd and Even Sums
Difficulty: Easy

Approach: [Your approach here]
"""

```python
import math
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

def gcdOfSumOddAndEven(count):
    sumOdd = count ** 2
    sumEven = count * (count + 1)
    # Handle edge case
    return math.gcd(sumOdd, sumEven)

# Time complexity: O(1)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
