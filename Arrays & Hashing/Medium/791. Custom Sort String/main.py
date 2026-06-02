from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # There can be duplicates - a good question to ask
        frequency_s = Counter(s)

        str_ = ""
        for char in order: # this will preserve the order of the characters and you just perform a lookup below
            if char not in frequency_s:
                continue
            str_ += char * frequency_s[char]
            del frequency_s[char]
        
        for char, count in frequency_s.items():
            str_ += char * count
        
        return str_
