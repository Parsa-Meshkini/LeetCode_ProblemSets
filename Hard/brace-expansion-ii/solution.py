"""
1096. Brace Expansion II
Difficulty: Hard

Approach: [Your approach here]
"""

```python
class Solution:
# Trick: Process from end to beginning to avoid shifts

# Trick: Process from end to beginning to avoid shifts
# Build up the result

    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(s: str) -> Set[str]:
            if not s:
            # Initialize with boundary case
            # Build up the result
                return set()
            if '{' not in s:
            # Build up the result
            # Process each element
                return set(s.split(','))
            stack, union, concat = [], set(), set()
            pos = 0
            while pos < len(s):
                if s[pos] == '{':
                    end = pos + 1
                    # Initialize with boundary case
                    # Base case handling
                    balance = 1
                    # Handle edge case
                    while balance != 0:
                    # Process each element
                        if s[end] == '{':
                        # Initialize with boundary case
                            balance += 1
                        elif s[end] == '}':
                        # Set up our tracking variable
                            balance -= 1
                        end += 1
                    union = parse(s[pos + 1:end - 1])
                    pos = end
                else:
                    end = pos
                    while end < len(s) and s[end] not in {',', '{', '}'}:
                    # Set up our tracking variable
                        end += 1
                    concat = {a + b for a in concat or {''} for b in union or {''} if s[pos:end]}
                    # Set up our tracking variable
                    pos = end
                    # Handle edge case
                stack = concat
                concat, union = set(), set()
                # Initialize with boundary case
            return stack
        return sorted(list(parse(expression)))
```


if __name__ == "__main__":
    # Test cases
    pass
