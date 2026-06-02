# The question wants you to find the longest substring containing the
# same letter that can be flipped. You need to examine the number of
# chars that can be flipped in the LOCAL window as opposed to the
# entire string.
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = ans = 0
        window = defaultdict(int)

        for right in range(len(s)): # O(n)
            # Add new character to window
            window[s[right]] = window.get(s[right], 0) + 1
            
            # curr = number of chars we need to replace
            # window length - count of most frequent char
            curr = (right - left + 1) - max(window.values()) # O(26)-> 0(1)

            # If we need more replacements than k allows
            while curr > k: # O(N) amoritzed
                window[s[left]] -= 1
                left += 1
                curr -= 1  # Simply decrement by 1 since window size reduced by 1
                
            ans = max(ans, right - left + 1)
            
        return ans