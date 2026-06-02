from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        window_size = len(words[0])
        concated_words_freq = Counter(words)

        for start in range(window_size):
            left, curr = start, defaultdict(int)
            for i in range(start, len(s) + 1, window_size):
                window = s[i - window_size : i]

                # If empty string or string on start or end
                # not valid window size, ignore and move to
                # next iteration
                if not window or len(window) < window_size:
                    continue

                # Add to window
                curr[window] += 1

                # Criteria to shrink window (a.k.a constraining criteria):
                    # C1 - If combo not in concated_words_freq
                    # C2 - If curr[combo] > concated_words_freq[s[right]]
                while curr.get(window, 0) > concated_words_freq.get(window, 0):
                    left_window = s[left: left + window_size]
                    curr[left_window] -= 1
                    if curr[left_window] == 0:
                        del curr[left_window]
                    left += window_size

                if curr == concated_words_freq:
                    ans.append(left)

        return ans
