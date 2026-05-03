from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hashmap = Counter(magazine)
        ransome_note_hashmap = Counter(ransomNote)
        for key, val in ransome_note_hashmap.items():
            # Edge case - letter not in magazine
            if key not in magazine_hashmap:
                return False
            
            # Edge case - letter in magazine but not enough occurrences in magazine
            if val > magazine_hashmap[key]:
                return False

        return True