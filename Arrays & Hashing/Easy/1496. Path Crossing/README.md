# 1496. Path Crossing
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/path-crossing/

## 1. Algorithm Used

Coordinate tracking with a hash set — detect if any position is visited more than once.

## 2. How to Recognize the Pattern

- "detect if a path revisits a location" → store visited coordinates in a set → check before each move.
- Grid/coordinate problems with revisit detection map directly to a set of (x, y) tuples.

## 3. Why This Algorithm Fits

- O(n) time — one pass through the path string.
- O(n) space — at most n+1 coordinates stored in the set.
- Tuple hashing gives O(1) insert and lookup for coordinate pairs.

## 4. How It Works

Start at (0, 0) and add it to the visited set. For each direction character, compute the new position using a direction map. If the new position is already in the set, the path crosses — return True. Otherwise add it and continue.

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        dirs = {'N': (0,1), 'S': (0,-1), 'E': (1,0), 'W': (-1,0)}
        for c in path:
            dx, dy = dirs[c]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
```

The starting position (0, 0) must be added before the loop — returning to the origin also counts as crossing.
