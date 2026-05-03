from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = []
        for c in order:
            if c in freq:
                result.append(c * freq[c])
                del freq[c]
        for c, cnt in freq.items():
            result.append(c * cnt)
        return ''.join(result)
