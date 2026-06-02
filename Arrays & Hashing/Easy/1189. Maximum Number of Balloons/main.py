from collections import Counter, defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Time complexity O(N) and Space complexity O(N)
        text_hashmap = defaultdict(int)
        balloon_hashset = Counter("balloon")
        
        # Construct frequency count for text
        for char in text:
            if char in balloon_hashset:
                text_hashmap[char] += 1

        # Early exit if missing any letters
        if len(text_hashmap) != len(balloon_hashset):
            return 0
        
        # Determine number letters that can be used from text
        for key, val in text_hashmap.items():
            text_hashmap[key] = val // balloon_hashset[key]
        
        return min(text_hashmap.values())

        # # More elegant solution with TC O(N) and SC O(1)
        # b = text.count('b')
        # a = text.count('a')
        # l = text.count('l')//2
        # o = text.count('o')//2
        # n = text.count('n')
        # return min(b,a,l,o,n)
