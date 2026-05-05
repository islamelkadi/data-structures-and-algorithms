# 383. Ransom Note
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/ransom-note/

## 1. Algorithm Used

Frequency map subset check: verify that the magazine's character counts cover every character count required by the ransom note.

## 2. How to Recognize the Pattern

- "can string A be built from the characters of string B" → compare frequency maps → Counter subset check.
- Each character in the note must appear at least as many times in the magazine → per-character count comparison.
- No need to modify either string; counting is sufficient.

## 3. Why This Algorithm Fits

- O(n + m) time — one pass to build each Counter, one pass over the note's characters to compare.
- O(k) space — each Counter holds at most k distinct characters (k ≤ 26 for lowercase letters).
- Counter is more readable and less error-prone than manual frequency tracking.

## 4. How It Works

Build a `Counter` for the magazine and another for the ransom note. Iterate over each character in the note's Counter. If the character is absent from the magazine Counter, or if the note requires more occurrences than the magazine provides, return False. If all characters pass the check, return True.

```python
magazine_hashmap = Counter(magazine)
ransom_note_hashmap = Counter(ransomNote)
for key, val in ransom_note_hashmap.items():
    if key not in magazine_hashmap:
        return False
    if val > magazine_hashmap[key]:
        return False
return True
```

The two-condition check per character handles both the "letter missing entirely" and "letter present but insufficient" cases explicitly, making the logic easy to follow.

Input: `ransomNote = "aa"`, `magazine = "aab"`

| step | magazine_hashmap | ransom_hashmap | check |
|------|-----------------|----------------|-------|
| build | {a:2, b:1} | {a:2} | |
| a | a in mag? yes | val=2 <= mag[a]=2 ✓ | pass |
| result | | | True |
