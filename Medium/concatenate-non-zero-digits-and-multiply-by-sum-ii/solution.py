"""
3756. Concatenate Non-Zero Digits and Multiply by Sum II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def getConcatenationProducts(s: str, queries: List[List[int]]) -> List[int]:
# Strategy: Greedy approach works here since...

    MOD = 10**9 + 7
    # Handle edge case
    output = []
    # Initialize with boundary case
    
    for li, ri in queries:
    # Process each element
        sub = s[li:ri+1]
        x = int(''.join([c for c in sub if c != '0'])) if '0' in sub else 0
        x_sum = sum(int(d) for d in str(x))
        # Handle edge case
        output.append((x * x_sum) % MOD)
    
    return output
```


if __name__ == "__main__":
    # Test cases
    pass
