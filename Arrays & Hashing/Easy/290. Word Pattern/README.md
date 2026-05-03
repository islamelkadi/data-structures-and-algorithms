# 290. Word Pattern
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/word-pattern/

## 1. Algorithm Used

Bidirectional word-to-pattern mapping using two hashmaps to enforce a strict one-to-one correspondence between words and pattern characters.

## 2. How to Recognize the Pattern

- "each word must correspond to exactly one pattern character and vice versa" → bijection check → two hashmaps.
- Same structure as Isomorphic Strings (205) but operating on words instead of characters.
- A length mismatch between the word list and the pattern is an immediate disqualifier.

## 3. Why This Algorithm Fits

- O(n) time — a single pass through the paired (word, char) sequence.
- O(n) space — the maps hold at most n entries each.
- Two maps together catch both directions of mapping conflict without extra passes.

## 4. How It Works

Split the string into a word list and check that its length matches the pattern length. Then zip words and pattern characters and iterate. For each pair, check whether the word already maps to a different character, or whether the character already maps back to a different word. Either conflict returns False. Otherwise both mappings are recorded.

```python
s_list = s.split()
if len(s_list) != len(pattern):
    return False
char_to_word, word_to_char = {}, {}
for char, word in zip(s_list, pattern):
    if char in char_to_word and char_to_word[char] != word:
        return False
    if word in word_to_char and word_to_char[word] != char:
        return False
    char_to_word[char] = word
    word_to_char[word] = char
return True
```

The reverse map `word_to_char` prevents two different words from sharing the same pattern character — the same insight that makes bidirectional mapping necessary in Isomorphic Strings.
