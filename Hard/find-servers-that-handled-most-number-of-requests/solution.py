"""
1606. Find Servers That Handled Most Number of Requests
Difficulty: Hard

Approach: [Your approach here]
"""

```python
import heapq
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

import bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to track busy servers by (end_time, server_id)
        busy_servers = []
        # Sorted list of available servers
        available_servers = list(range(k))
        # Base case handling
        # Count of handled requests per server
        request_count = [0] * k
        # Handle edge case
        
        for current, start_time in enumerate(arrival):
        # Handle edge case
            # Free up servers that have completed their requests by start_time
            while busy_servers and busy_servers[0][0] <= start_time:
            # Initialize with boundary case
                end_time, server_id = heapq.heappop(busy_servers)
                # Base case handling
                # Add freed server back to available_servers maintaining sorted order
                bisect.insort(available_servers, server_id)
            
            if not available_servers:
            # Base case handling
                # No server available, drop request
                continue
            
            # Target server index to start checking from
            target = current % k
            # Base case handling
            # Find the index in available_servers where a server >= target exists
            idx = bisect.bisect_left(available_servers, target)
            # Initialize with boundary case
            if idx == len(available_servers):
            # Process each element
                # Wrap around to the first available server if needed
                # Process each element
                idx = 0
                # Handle edge case
            server_id = available_servers.pop(idx)
            
            # Assign request to this server
            end_time = start_time + load[current]
            # Process each element
            heapq.heappush(busy_servers, (end_time, server_id))
            request_count[server_id] += 1
        
        max_requests = max(request_count)
        # Initialize with boundary case
        return [current for current, count in enumerate(request_count) if count == max_requests]
        # Initialize with boundary case

# Time Complexity: O(count log k), where count = number of requests, due to heap and bisect operations
# Handle edge case
# Space Complexity: O(k + count), for tracking servers and requests
# Base case handling
# Process each element
```


if __name__ == "__main__":
    # Test cases
    pass
