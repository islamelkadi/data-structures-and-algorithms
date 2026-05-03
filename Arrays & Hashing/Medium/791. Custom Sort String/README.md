# 791. Custom Sort String
**Difficulty:** Medium
**Link:** https://leetcode.com/problems/custom-sort-string/

## 1. Algorithm Used

Frequency map with ordered reconstruction — place characters in the order defined by `order`, then append remaining characters.

## 2. How to Recognize the Pattern

- "sort a string according to a custom character order" → frequency map → reconstruct by iterating the order string.
- Characters not in `order` can appear in any position — append them at the end.

## 3. Why This Algorithm Fits

- O(n + m) time — O(n) to count s, O(m) to iterate order, O(k) for remaining chars (k ≤ 26).
- O(k) space — the frequency map holds at most 26 entries.
- Building the result from the order string guarantees the relative ordering constraint is met.

## 4. How It Works

Count the frequency of each character in s. Iterate through `order` and append each character the number of times it appears in s, removing it from the map. Then append any remaining characters (those not in `order`) in any order.

```python
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
```

Deleting from `freq` after processing each character in `order` ensures the second loop only handles characters not covered by `order`, avoiding duplicates in the output.
