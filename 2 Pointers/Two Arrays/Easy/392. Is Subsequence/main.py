from collections import defaultdict
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) > len(t):
            return False

        if not s:
            return True
        # The idea here is that you have a left pointer
        # that only moves when there is a match, while
        # there is a right pointer that moves with each
        # iteration. If the character in t matches the
        # letter at the left pointer index of s, then you
        # have a match and you increment the pointer. This
        # algorithm accounts for the order as well, because
        # you are only incrementing on the first match. Meaning
        # If you you are iterating over a char from t, and it is
        # not in the current left index position becuase it has not
        # arrived yet, then you will never match and therefore
        # never increment. The order matters because you are
        # forming a subsequence where the order matters too! 
        slow_pointer = 0
        for char in t:
            if char == s[slow_pointer]:
                slow_pointer += 1
            if slow_pointer == len(s):
                return True
        return False