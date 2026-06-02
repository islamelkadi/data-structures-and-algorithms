class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        english_letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
        english_letters_uppercase = english_letters_lowercase.upper()
        english_letters = english_letters_lowercase + english_letters_uppercase

        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            left_is_english = s[left] in english_letters
            right_is_english = s[right] in english_letters

            if not left_is_english:
                left += 1
                continue
            elif not right_is_english:
                right -= 1
                continue
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
