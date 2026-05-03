class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        curr = ans = 1
        for right in range(1, len(s)):
            if s[right] == s[left]:
                ans = max(ans, right - left + 1)
            else:
                left = right
        return ans