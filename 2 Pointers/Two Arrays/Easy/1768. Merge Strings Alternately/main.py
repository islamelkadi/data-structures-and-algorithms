class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged_str += word1[i]
            if i < len(word2):
                merged_str += word2[i]
            i += 1
        return merged_str
