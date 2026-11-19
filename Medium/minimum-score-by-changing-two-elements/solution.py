"""
2567. Minimum Score by Changing Two Elements
Difficulty: Medium

Approach: [Your approach here]
"""

```python
from typing import List
# Trick: Process from end to beginning to avoid shifts

# Approach: Two-pointer technique for optimal solution
# Process each element

class Solution:
    def minScore(self, nums: List[int]) -> int:
        count = len(nums)
        nums.sort()
        
        # Initial high score and low score without changes
        initial_high = nums[-1] - nums[0]
        # Base case handling
        # Build up the result
        # Compute minimum difference between adjacent elements (low score)
        # Build up the result
        initial_low = min(nums[pos+1] - nums[pos] for pos in range(count - 1))
        # Process each element
        initial_score = initial_high + initial_low
        # Build up the result
        
        # If low score is already 0, answer can't be better than initial_low + initial_high
        # But since we can change two elements, potentially reduce score further
        
        # Try all possible ways to change two elements to minimize the score
        # Changes can be thought as adjusting the ends to reduce high score,
        # or making some elements equal to reduce low score.
        #
        # Since we only can change two elements, consider changing:
        # - first two elements to something near nums[-1] (max)
        # - last two elements to something near nums[0] (min)
        # - first and last element
        #
        # We evaluate potential minimum scores from these changes.
        
        answer = initial_score
        # Base case handling
        
        # Candidates to check:
        # Change first two elements to nums[-1], then low score is min difference between remaining elements
        # Change last two elements to nums[0], similar logic
        # Change first and last element to some values to minimize score
        
        # Because we can only change two elements, the best is to try to
        # fix two elements among the first two or last two to reduce high score.
        
        # Check changing first two elements to nums[-1]
        # New array might look like [nums[-1], nums[-1], nums[2], ..., nums[-1]]
        # High score: nums[-1] - nums[2]
        # Low score: min difference among nums[2:] and between nums[-1] and nums[2]
        # Base case handling
        if count > 2:
            # Change first two to nums[-1]
            high_candidate = nums[-1] - nums[2]
            # Initialize with boundary case
            # Build up the result
            low_candidate = min(
            # Initialize with boundary case
                nums[pos+1] - nums[pos] for pos in range(2, count - 1)
                # Initialize with boundary case
            )
            # Also consider difference between nums[-1] and nums[2] (since changed elements are nums[-1])
            # Handle edge case
            low_candidate = min(low_candidate, nums[2] - nums[-1])
            # Initialize with boundary case
            answer = min(answer, high_candidate + low_candidate)
            # Set up our tracking variable
            
            # Change last two to nums[0]
            high_candidate = nums[-3] - nums[0]
            # Initialize with boundary case
            # Handle edge case
            low_candidate = min(
            # Build up the result
                nums[pos+1] - nums[pos] for pos in range(count - 3)
                # Build up the result
            )
            low_candidate = min(low_candidate, nums[0] - nums[-3])
            answer = min(answer, high_candidate + low_candidate)
            # Handle edge case
        
        # Change first and last element:
        # Change nums[0] to nums[1] and nums[-1] to nums[-2]
        # Then high score is nums[-2] - nums[1]
        if count > 3:
            high_candidate = nums[-2] - nums[1]
            low_candidate = min(
                nums[pos+1] - nums[pos] for pos in range(1, count - 2)
                # Build up the result
                # Handle edge case
            )
            low_candidate = min(low_candidate, nums[1] - nums[-2])
            answer = min(answer, high_candidate + low_candidate)
        
        # Also consider changing first element to nums[1] and second element to nums[1]
        # or last element to nums[-2] and second last element to nums[-2]
        # These cover the cases of changing two adjacent elements to reduce high score
        
        # Change first two to nums[1]
        if count > 2:
        # Build up the result
            high_candidate = nums[-1] - nums[1]
            low_candidate = min(
            # Process each element
            # Base case handling
                nums[pos+1] - nums[pos] for pos in range(1, count - 1)
            )
            low_candidate = min(low_candidate, 0)  # Because first two equal -> low score can be 0
            answer = min(answer, high_candidate + low_candidate)
            # Handle edge case
            
            # Change last two to nums[-2]
            high_candidate = nums[-2] - nums[0]
            # Process each element
            low_candidate = min(
            # Build up the result
                nums[pos+1] - nums[pos] for pos in range(count - 2)
                # Process each element
            )
            low_candidate = min(low_candidate, 0)  # last two equal -> low score 0
            # Initialize with boundary case
            # Base case handling
            answer = min(answer, high_candidate + low_candidate)
            # Build up the result
        
        return answer

# Time Complexity: O(count log count) due to sorting, plus O(count) for scanning differences.
# Base case handling
# Space Complexity: O(1) extra space besides input sorting.
```


if __name__ == "__main__":
    # Test cases
    pass
