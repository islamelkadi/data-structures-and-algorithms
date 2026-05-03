from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Early exit
        if len(s) != len(t):
            return False

        s_hashset = Counter(s)
        t_hashset = Counter(t)
        for char, val in t_hashset.items():
            if s_hashset[char] != val:
                return False
        return True