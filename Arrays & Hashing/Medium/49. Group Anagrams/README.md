## 1. Algorithm Used

Hash Map grouping with two key-generation strategies: sorted string (Option 1) and character frequency array (Option 2).

## 2. How to Recognize the Pattern

- "Group words that are anagrams" → same characters, same counts → need a canonical key per group.
- Multiple items need to be bucketed by a shared property → hash map with a derived key.
- The choice is how to compute that key: sorting vs counting.

## 3. Why This Algorithm Fits

- Both options are single-pass over the word list with a hash map for grouping.
- Option 1: O(n · k log k) time, key is a sorted string.
- Option 2: O(n · k) time, key is a frequency tuple.
- Both use O(n · k) space for storing the groups.

## 4. How It Works

For each word, generate a canonical key that's identical for all anagrams. Use that key in a defaultdict to group words together. Return all groups.

Option 1 — sort the word:
```python
ordered_word = "".join(sorted(word))
anagram_hashmap[ordered_word].append(word)
```

Option 2 — count character frequencies:
```python
word_chars_index = [0] * 26
for str_ in word:
    word_chars_index[ord(str_) - ord("a")] += 1
anagram_hashmap[tuple(word_chars_index)].append(word)
```

## 5. Trade-offs

Option 1 (sorting):
- Simpler, more readable
- Key is a plain string — lightweight and easy to hash
- O(k log k) per word, but for short words the constant factor is tiny

Option 2 (frequency array):
- O(k) per word — better asymptotic complexity
- But you allocate a 26-element list per word, convert it to a tuple, then hash a 26-element tuple
- Tuple hashing is more expensive than string hashing — Python has to hash 26 integers vs a compact string
- More memory overhead per key (26 ints vs a short string)

So the irony: Option 2 wins on paper (O(k) vs O(k log k)), but Option 1 often performs just as well or better in practice for short words because string sorting and hashing are highly optimized in Python. Option 2 becomes the clear winner only when words are long.