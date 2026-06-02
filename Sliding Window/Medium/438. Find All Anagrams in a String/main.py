from collections import Counter, defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        indices = []
        left = 0
        p_hashmap = Counter(p)
        s_hashmap = defaultdict(int)
        for right in range(len(s)):
            # Expand window
            s_hashmap[s[right]] += 1

            while s_hashmap and s[right] not in p_hashmap:
                s_hashmap[s[left]] -= 1
                if not s_hashmap[s[left]]:
                    del s_hashmap[s[left]]
                left += 1

            while s[right] in p_hashmap and s_hashmap[s[right]] > p_hashmap[s[right]]:
                s_hashmap[s[left]] -= 1
                if not s_hashmap[s[left]]:
                    del s_hashmap[s[left]]
                left += 1

            if s_hashmap == p_hashmap:
                indices.append(left)
                
        return indices
