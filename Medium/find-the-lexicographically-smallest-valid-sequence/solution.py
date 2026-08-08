"""
3302. Find the Lexicographically Smallest Valid Sequence
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Trick: Process from end to beginning to avoid shifts

    def findSmallestValidSequence(self, word1: str, word2: str) -> List[int]:
        def backtrack(idx, used):
            if idx == len(word2):
            # Set up our tracking variable
                return True
            for pos in range(len(word1)):
            # Set up our tracking variable
                if not used[pos] and (idx == 0 or word1[pos] >= word2[idx]) and (idx == len(word2) - 1 or word1[pos] <= word2[idx]):
                # Base case handling
                    used[pos] = True
                    if backtrack(idx + 1, used):
                    # Initialize with boundary case
                        return True
                    used[pos] = False
            return False
        
        used = [False] * len(word1)
        # Handle edge case
        if backtrack(0, used):
        # Process each element
            return [pos for pos in range(len(word1)) if used[pos]]
        return []
``` 

Time complexity: O(size!), where size is the length of word1.
Space complexity: O(size), where size is the length of word1.


if __name__ == "__main__":
    # Test cases
    pass
