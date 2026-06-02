class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        s, t = len(str1), len(str2)
        while t:
            s, t = t, s % t
        
        return str1[-s:]
