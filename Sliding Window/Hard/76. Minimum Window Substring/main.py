from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(s) < len(t):
            return ""
        if s == t:
            return s

        # Initialize variables
        t_length = len(t)
        t_hashmap = Counter(t)
        s_hashmap = defaultdict(int)
        ans = float("inf")
        curr = left = left_boundary = 0

        for right in range(len(s)):
            # Expand window
            # Add EACH character to the hashmap but only increase CURR if s[right] is in t_hashmap
            # this becomes important in the shrinking window component. If you only add to s_hashmap
            # the characters that are in t_hashmap, then when it's trim to decrease the window and
            # you do a s_hashmap[s[left]] where s[left] is from the s string, you are decreasing the
            # count of s_hashmap[s[left]] where s[left] is NOT in t_hashmap to -1. Therefore, even
            # when s_hashmap[s[left]] is not in t_hashmap the condition that decrements curr will
            # always be true as -1 < 0. Therefore; you are incorrectly decrementing the count.
            if s[right] in t_hashmap:
                s_hashmap[s[right]] += 1 
                if s_hashmap[s[right]] <= t_hashmap[s[right]]:
                    curr += 1

            # Shrink window
            while curr == t_length:

                # Update answer if smaller window found
                if right - left + 1 < ans:
                    ans = right - left + 1
                    left_boundary = left

                # Shrink the window
                if s[left] in s_hashmap:
                    s_hashmap[s[left]] -= 1
                    if s_hashmap[s[left]] < t_hashmap[s[left]]:
                        curr -= 1
                left += 1

        return "" if ans == float("inf") else s[left_boundary: left_boundary + ans]

# from collections import defaultdict, Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # Edge cases
#         if not s or not t or len(s) < len(t):
#             return ""
#         if s == t:
#             return s

#         # Initialize variables
#         t_length = len(t)
#         t_hashmap = Counter(t)
#         s_hashmap = defaultdict(int)
#         ans = float("inf")
#         curr = left = left_boundary = 0

#         for right in range(len(s)):
#             # Expand window
#             # Add EACH character to the hashmap but only increase CURR if s[right] is in t_hashmap
#             # this becomes important in the shrinking window component. If you only add to s_hashmap
#             # the characters that are in t_hashmap, then when it's trim to decrease the window and
#             # you do a s_hashmap[s[left]] where s[left] is from the s string, you are decreasing the
#             # count of s_hashmap[s[left]] where s[left] is NOT in t_hashmap to -1. Therefore, even
#             # when s_hashmap[s[left]] is not in t_hashmap the condition that decrements curr will
#             # always be true as -1 < 0. Therefore; you are incorrectly decrementing the count.
#             s_hashmap[s[right]] += 1 
#             if s_hashmap[s[right]] <= t_hashmap[s[right]]:
#                 curr += 1

#             # Shrink window
#             while curr == t_length:
#                 # Update answer if smaller window found
#                 if right - left + 1 < ans:
#                     ans = right - left + 1
#                     left_boundary = left

#                 # Shrink the window
#                 s_hashmap[s[left]] -= 1
#                 if s_hashmap[s[left]] < t_hashmap[s[left]]:
#                     curr -= 1
#                 left += 1

#         return "" if ans == float("inf") else s[left_boundary: left_boundary + ans]