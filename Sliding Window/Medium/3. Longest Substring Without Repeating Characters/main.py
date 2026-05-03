from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # Option 1 - using hashmap
        # left = ans = 0
        # curr = defaultdict(int)
        # for i in range(len(s)):
        #     curr[s[i]] += 1
        #     while curr[s[i]] > 1:
        #         curr[s[left]] -= 1
        #         left += 1
        #     ans = max(ans, i - left + 1)
        # return ans
    
        # Option 2 - using hashset
        left = ans = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            ans = max(ans, i - left + 1)
        return ans