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
