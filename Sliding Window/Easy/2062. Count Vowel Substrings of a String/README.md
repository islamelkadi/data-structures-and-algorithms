# 2062. Count Vowel Substrings of a String

**Difficulty:** Easy
**Link:** [LeetCode URL](https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/)

## Table of Contents
1. [Algorithm Used](#1-algorithm-used)
2. [How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [How It Works](#4-how-it-works)

## 1. Algorithm Used

The algorithm uses a Sliding Window with the **Exactly $K$** distinct elements constraint solved via subtraction of **At Most $K$** configurations:
$$\text{exactly}(K) = \text{at\_most}(K) - \text{at\_most}(K - 1)$$
Here, we compute the number of substrings containing only vowels with exactly 5 unique vowels by calculating:
$$\text{at\_most}(5) - \text{at\_most}(4)$$

## 2. How to Recognize the Pattern

- **Substrings with exactly $K$ unique elements**: Whenever a problem asks for substrings or subarrays containing *exactly* a certain number of unique elements (e.g., all 5 vowels), it is difficult to cleanly shrink the window from the left. Using the identity $\text{exact}(K) = \text{at\_most}(K) - \text{at\_most}(K-1)$ allows us to run standard sliding window algorithms twice and subtract their results.
- **Invalid characters reset window**: The constraint specifies that the substring must contain *only* vowels. Therefore, when encountering a non-vowel, the sliding window must be immediately reset.

## 3. Why This Algorithm Fits

- **Time Complexity**: $O(N)$ — We execute two sliding window passes over the string of length $N$. Each pass processes each character at most twice (once by the `right` pointer, and at most once by the `left` pointer).
- **Space Complexity**: $O(1)$ — The frequency map stores at most 5 vowel keys at any given time, which takes constant auxiliary space.

## 4. How It Works

1. Define a helper function `countVowelAtmostSubstrings(word, k)` that counts substrings containing only vowels and at most `k` unique vowels.
2. Inside the helper, iterate the `right` pointer over the word:
   - If `word[right]` is not a vowel, reset the window: clear the frequency map `curr` and move the `left` pointer to `right + 1`. This prepares the window for the next iteration.
   - Otherwise, record the vowel frequency in `curr`.
   - While the number of unique vowels in `curr` exceeds `k` (`len(curr) > k`), decrement the count of `word[left]`. If the count of that vowel hits `0`, delete it from `curr`. Increment `left`.
   - Add `right - left + 1` (the number of valid substrings ending at `right`) to `ans`.
3. Return the result of `countVowelAtmostSubstrings(word, 5) - countVowelAtmostSubstrings(word, 4)`.

> [!IMPORTANT]
> **Implementation Note on Window Reset**:
> When a non-vowel is encountered at index `right`, we assign `left = right + 1` and clear `curr`. This moves the left index to be in the position of where the right index will be after the `continue` statement, ensuring no substrings containing invalid (non-vowel) characters are counted in our range.

```python
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
```

### Dry Run Table
Tracing `countVowelAtmostSubstrings(word, 2)` for `word = "aei"`:

| Step/Index (`right`) | `word[right]` | Action / Condition | Window `[left, right]` | `curr` | `ans` |
|----------------------|---------------|-------------------|------------------------|--------|-------|
| *init*               | —             | —                 | —                      | `{}`   | 0     |
| 0                    | 'a'           | Add to dict       | `[0, 0]` (`"a"`)       | `{'a': 1}` | 1     |
| 1                    | 'e'           | Add to dict       | `[0, 1]` (`"ae"`)      | `{'a': 1, 'e': 1}` | 3 |
| 2                    | 'i'           | Add to dict, exceed `k=2` | —              | `{'a': 1, 'e': 1, 'i': 1}` | 3 |
| 2 (shrink)           | —             | Pop `word[0]` ('a'), `left` $\to$ 1 | `[1, 2]` (`"ei"`) | `{'e': 1, 'i': 1}` | 5 |
