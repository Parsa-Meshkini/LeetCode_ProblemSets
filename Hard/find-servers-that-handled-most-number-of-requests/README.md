# 1606. Find Servers That Handled Most Number of Requests

**Difficulty:** Hard
**Date:** 1606

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests)

## Solution Approach

The approach tracks each server's next available time and assigns incoming requests to the smallest-indexed server that is free at the request time, using a balanced data structure (e.g., a TreeSet or priority queue) to efficiently find and update available servers. This works efficiently by avoiding scanning all servers per request, reducing complexity from O(nk) to O(k log n), where n is servers and k is requests.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
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
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
