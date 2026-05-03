class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Need a mechanism to map each letter to it's counter part
        # Need a mechanism to check if current letter (that's already mapped) has a different counter part
            # If so - return False
        # Need a mechanism to check if an s letter maps to a t letter used by another s letter
        
        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            if s[i] in s_hashmap and s_hashmap[s[i]] != t[i]:
                return False

            elif t[i] in t_hashmap and t_hashmap[t[i]] != s[i]:
                return False

            s_hashmap[s[i]] = t[i]
            t_hashmap[t[i]] = s[i]

        return True