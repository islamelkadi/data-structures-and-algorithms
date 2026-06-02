class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        left = 0
        right = final = word.index(ch)
        sub_word = list(word[:right+1])
        while left < right:
            sub_word[left], sub_word[right] = sub_word[right], sub_word[left]
            left += 1
            right -= 1
        return "".join(sub_word) + word[final+1:]
