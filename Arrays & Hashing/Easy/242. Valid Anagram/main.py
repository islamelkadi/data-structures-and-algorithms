from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_hashmap = Counter(s)
        # t_hashmap = Counter(t)
        # return s_hashmap == t_hashmap
        # Contruct counter of s

        # Edge case for early return
        # if the lengths of S & T don't
        # match, because that means they
        # aren't anagrams.
        if len(s) != len(t):
            return False

        # Create dict of chars and frequency
        # for S
        s_hashmap = defaultdict(int)
        for char in s:
            s_hashmap[char] += 1

        # Cross reference chars of t and it's
        # frequency with S. If the a char in
        # T is not in S, then they aren't
        # anagrams.
        for char in t:
            if s_hashmap.get(char, 0) == 0:
                return False
            s_hashmap[char] -= 1

        return True