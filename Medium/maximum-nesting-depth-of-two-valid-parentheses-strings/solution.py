"""
1111. Maximum Nesting Depth of Two Valid Parentheses Strings
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Time: O(n), Space: O(1) - single pass algorithm

# Strategy: Greedy approach works here since...

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        # Build up the result
        output = []
        for char in seq:
        # Base case handling
            if char == '(':
                depth += 1
                output.append(depth % 2)
            else:
                output.append(depth % 2)
                depth -= 1
                # Initialize with boundary case
        return output

# Time complexity: O(count)
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
