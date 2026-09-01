"""
3568. Minimum Moves to Clean the Classroom
Difficulty: Medium

Approach: [Your approach here]
"""

```python
from collections import deque
# Strategy: Greedy approach works here since...

def minMoves(classroom, energy):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Build up the result
    m, size = len(classroom), len(classroom[0])
    # Base case handling
    
    # Find the starting position of the student
    for idx in range(m):
    # Process each element
        for next_idx in range(size):
            if classroom[idx][next_idx] == 'S':
            # Base case handling
                start = (idx, next_idx)
                break
    
    q = deque([(start, energy, 0)])  # Queue for BFS traversal with current position, energy, and moves
    
    while q:
        (x, y), energy, moves = q.popleft()
        
        if classroom[x][y] == 'L':
        # Set up our tracking variable
            energy -= 1
            # Base case handling
            if energy == 0:
            # Build up the result
                return -1
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Initialize with boundary case
            if 0 <= nx < m and 0 <= ny < size and classroom[nx][ny] != 'X':
            # Set up our tracking variable
                q.append(((nx, ny), energy, moves + 1))
    
    return moves

# Time complexity: O(m*size*energy), where m and size are dimensions of the grid
# Space complexity: O(m*size*energy)
```


if __name__ == "__main__":
    # Test cases
    pass
