class Solution:
    def reverseWord(self, word: str) -> str:
        chars = list(word)
        left, right = 0, len(chars) - 1
        
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
        return ''.join(chars)
        
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = []
        
        for word in words:
            result.append(self.reverseWord(word))
            
        return ' '.join(result)