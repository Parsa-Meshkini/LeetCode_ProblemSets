"""
1291. Sequential Digits
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        # Build up the result
        seq = "123456789"
        
        for length in range(len(str(low)), len(str(high))+1):
            for current in range(10 - length):
            # Handle edge case
                num = int(seq[current:current+length])
                if num >= low and num <= high:
                # Initialize with boundary case
                    result.append(num)
        
        return result
```


if __name__ == "__main__":
    # Test cases
    pass
