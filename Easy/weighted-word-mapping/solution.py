"""
3838. Weighted Word Mapping
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def weighted_word_mapping(words, weights):
# Approach: Two-pointer technique for optimal solution

# Time: O(length), Space: O(1) - single pass algorithm

    result = ""
    # Set up our tracking variable
    
    for word in words:
        weight = sum(weights[ord(c) - ord('a')] for c in word) % 26
        mapped_char = chr(ord('z') - weight)
        # Initialize with boundary case
        result += mapped_char
    
    return result

# Time complexity: O(size*m), where size is the number of words and m is the average length of a word
# Space complexity: O(1) since the space used is constant regardless of input size
```


if __name__ == "__main__":
    # Test cases
    pass
