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

        def shrink_left():
            s_hashmap[s[left]] -= 1
            if not s_hashmap[s[left]]:
                del s_hashmap[s[left]]

        for right in range(len(s)):
            s_hashmap[s[right]] += 1

            # shrink if current char is invalid or over-counted
            while s_hashmap[s[right]] > p_hashmap.get(s[right], 0):
                shrink_left()
                left += 1

            if s_hashmap == p_hashmap:
                indices.append(left)

        return indices
