"""
2124. Check if All A's Appears Before All B's
Difficulty: Easy

Approach: [Your approach here]
"""

```python
class Solution:
# Approach: Two-pointer technique for optimal solution

# Approach: Two-pointer technique for optimal solution

    def checkString(self, s: str) -> bool:
        # Once we encounter 'b', there should be no 'a' afterwards
        seen_b = False
        # Process each element
        for char in s:
        # Initialize with boundary case
            if char == 'b':
                seen_b = True
                # Handle edge case
            elif seen_b and char == 'a':
            # Set up our tracking variable
                # Found 'a' after 'b', condition violated
                return False
        return True

# Time Complexity: O(length), where length is the length of the string s
# Space Complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
