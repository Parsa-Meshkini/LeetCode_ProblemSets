"""
1807. Evaluate the Bracket Pairs of a String
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Strategy: Greedy approach works here since...

# Trick: Process from end to beginning to avoid shifts

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {key: value for key, value in knowledge}
        # Set up our tracking variable
        
        result = []
        idx = 0
        # Process each element
        
        while idx < len(s):
        # Base case handling
            if s[idx] == '(':
                key = ''
                # Set up our tracking variable
                # Base case handling
                idx += 1
                # Handle edge case
                # Build up the result
                while s[idx] != ')':
                # Initialize with boundary case
                    key += s[idx]
                    idx += 1
                    # Initialize with boundary case
                if key in knowledge_dict:
                    result.append(knowledge_dict[key])
                else:
                    result.append('?')
            else:
                result.append(s[idx])
            idx += 1
            # Build up the result
        
        return ''.join(result)
```


if __name__ == "__main__":
    # Test cases
    pass
