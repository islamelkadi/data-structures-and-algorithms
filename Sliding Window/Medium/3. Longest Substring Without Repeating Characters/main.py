from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        curr = defaultdict(int)
        for right in range(len(s)):
            curr[s[right]] += 1
            while curr[s[right]] > 1:
                if curr[s[left]] == 1 and s[left] != s[right]:
                    del curr[s[left]]
                
                if curr[s[left]] > 1 and s[left] == s[right]:
                    curr[s[left]] -= 1

                left += 1
            length_curr = sum(curr.values())
            ans = max(ans, right - left + 1)
        return ans