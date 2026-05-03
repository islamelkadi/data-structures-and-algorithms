class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Create hashset for direct lookup
        vowels = set("aeiouAEIOU")

        # Split string in preparation for 
        # switching as strs are immutable
        # in Python
        s = list(s)

        # Initialize 2 ptrs
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            
            if s[right] not in vowels:
                right -= 1
            
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)