# 1436. Destination City

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/destination-city/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm utilizes a Hash Map to record the directed path from each source city to its destination city. Cities that only appear as destinations but never as sources are mapped to `None`, making it simple to identify the final destination city in a single final scan.

## 2. How to Recognize the Pattern

- **Find node with zero out-degree**: In graph terminology, we are looking for the node with no outgoing edges. Whenever we need to associate nodes with their outgoing connections and test for the absence of outgoing edges, a Hash Map or a Hash Set of source nodes is the standard approach.
- **Hash Table vs Set**: While this can be solved using two sets (all destination cities minus all source cities), a Hash Map directly tracks the mapping and identifies the sink node cleanly.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ where $N$ is the number of path connections. Building the hash map takes $O(N)$ and searching the keys takes at most $O(N)$ time.
- **Space Complexity**: $O(N)$ auxiliary space to store the mappings of up to $2N$ unique cities.

## 4. How It Works

1. Initialize `city_paths = {}`.
2. Traverse through each directed path `[start, dest]` in `paths`:
   - Map `start` to `dest` in `city_paths`.
   - If `dest` does not already exist as a key in `city_paths`, initialize its value to `None` to indicate it currently has no known outgoing paths.
3. Iterate through `city_paths` items. The city whose mapped value is `None` has no outgoing path and is returned as the final destination city.

```python
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # USING HASHMAPS
        city_paths = {}
        for path in paths:
            city_paths[path[0]] = path[1]
            if path[1] not in city_paths:
                city_paths[path[1]] = None
        
        # Find city with None as destination:
        for start, destination in city_paths.items():
            if destination is None:
                return start
```

### Dry Run Table
Input: `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`

| Step/Index | Path `[start, dest]` | `city_paths` State | Action Taken |
|------------|---------------------|--------------------|--------------|
| *init*     | —                   | `{}`               | Initialize map |
| 0          | `["London","New York"]` | `{"London": "New York", "New York": None}` | Map London $\to$ New York; initialize New York $\to$ None |
| 1          | `["New York","Lima"]`   | `{"London": "New York", "New York": "Lima", "Lima": None}` | Map New York $\to$ Lima; initialize Lima $\to$ None |
| 2          | `["Lima","Sao Paulo"]`  | `{"London": "New York", "New York": "Lima", "Lima": "Sao Paulo", "Sao Paulo": None}` | Map Lima $\to$ Sao Paulo; initialize Sao Paulo $\to$ None |
| Search     | —                   | —                  | Scan items; find `"Sao Paulo"` maps to `None`. Return `"Sao Paulo"` |
