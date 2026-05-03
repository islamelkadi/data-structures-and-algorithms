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
