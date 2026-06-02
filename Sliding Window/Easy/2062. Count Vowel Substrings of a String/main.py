from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def countVowelAtmostSubstrings(word, k):
            left = ans = 0
            vowels = {"a","e","i","o","u"}
            curr = defaultdict(int)

            for right in range(len(word)):
                if word[right] not in vowels:
                    left = right + 1 # this is to move the left index to be in the position of where the right index will be after the continue statement
                    curr.clear()
                    continue

                curr[word[right]] += 1
                while len(curr) > k:
                    if word[left] in curr:
                        curr[word[left]] -= 1

                    if curr[word[left]] == 0:
                        del curr[word[left]]

                    left += 1
                ans += right - left + 1
            return ans
        return countVowelAtmostSubstrings(word, 5) - countVowelAtmostSubstrings(word, 4)
