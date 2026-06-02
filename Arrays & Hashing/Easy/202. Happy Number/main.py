class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen_hashset = set()
        while n != 1:
            if n in seen_hashset:
                return False
            seen_hashset.add(n)
            n = sum([int(x)**2 for x in str(n)])
        else:
            return True
