class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        # Edge case: number of words does not match number of chars
        if len(s_list) != len(pattern):
            return False

        # Look ups in two dicts
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(s_list, pattern):
            if char in char_to_word and char_to_word[char] != word:
                    return False
            elif word in word_to_char and word_to_char[word] != char:
                    return False    
            char_to_word[char] = word
            word_to_char[word] = char
        return True