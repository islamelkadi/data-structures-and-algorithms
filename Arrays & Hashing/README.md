# Arrays & Hashing


## Table of Contents
1. [1. What It Is](#1-what-it-is)
2. [2. When to Use It — Pattern Recognition](#2-when-to-use-it--pattern-recognition)
   - [Keywords that signal this algorithm:](#keywords-that-signal-this-algorithm)
   - [Problem characteristics:](#problem-characteristics)
3. [3. Core Technique(s)](#3-core-techniques)
   - [Technique A: Hash Set for O(1) Membership](#technique-a-hash-set-for-o1-membership)
   - [Technique B: Frequency Counter](#technique-b-frequency-counter)
   - [Technique C: Bidirectional Mapping (Bijection)](#technique-c-bidirectional-mapping-bijection)
   - [Technique D: Bucket Sort / Counting Sort](#technique-d-bucket-sort--counting-sort)
   - [Technique E: Computed Hash Key for Grouping](#technique-e-computed-hash-key-for-grouping)
4. [4. Decision Framework](#4-decision-framework)
5. [5. One-Pass vs Multi-Pass Reasoning](#5-one-pass-vs-multi-pass-reasoning)
6. [6. Index and Pointer Management](#6-index-and-pointer-management)
7. [7. Complexity Patterns](#7-complexity-patterns)
8. [8. Common Pitfalls](#8-common-pitfalls)

## 1. What It Is

Arrays & Hashing covers problems solved by trading space for time: store elements (or their frequencies, positions, or mappings) in a hash set or hash map to answer membership, frequency, and relationship queries in O(1) instead of O(n). The core idea is that a hash structure lets you look up "have I seen this before?" or "how many times did X appear?" in constant time.

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "duplicate" / "contains duplicate" → hash set membership check
- "anagram" / "permutation of" → frequency comparison (Counter)
- "frequency" / "count occurrences" → Counter or defaultdict
- "unique" / "distinct" → set for deduplication
- "common elements" / "intersection" → set intersection
- "group by" / "group anagrams" → hashmap with sorted key or tuple key
- "isomorphic" / "word pattern" / "bijection" → two hashmaps for bidirectional mapping
- "missing number" / "first missing" → set lookup

### Problem characteristics:
- You need to answer "does X exist?" repeatedly → hash set
- You need to count how many times each value appears → Counter / frequency map
- You need to map one set of values to another uniquely → two hashmaps
- You need to group items that share a property → hashmap with computed key
- Brute force would be O(n²) due to nested membership checks

## 3. Core Technique(s)

### Technique A: Hash Set for O(1) Membership

```python
seen = set()
for x in arr:
    if x in seen:
        return True   # duplicate found
    seen.add(x)
return False
```

Use when: contains duplicate, path crossing, cycle detection in happy number.

### Technique B: Frequency Counter

```python
from collections import Counter

freq = Counter(arr)          # {value: count}
# or equivalently:
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Use when: valid anagram, group anagrams, majority element, ransom note, unique occurrences.

**Anagram check**: two strings are anagrams iff `Counter(s) == Counter(t)`.

**Frequency shape comparison** (e.g., "close strings"): two arrays are "close" if they have the same set of keys and the same multiset of frequency values — check `set(freq1) == set(freq2)` and `sorted(freq1.values()) == sorted(freq2.values())`.

### Technique C: Bidirectional Mapping (Bijection)

For isomorphic strings and word patterns, you need a one-to-one mapping in both directions.

```python
s_to_t = {}
t_to_s = {}
for a, b in zip(s, t):
    if s_to_t.get(a, b) != b or t_to_s.get(b, a) != a:
        return False
    s_to_t[a] = b
    t_to_s[b] = a
return True
```

Use when: isomorphic strings, word pattern, any problem requiring a bijection.

### Technique D: Bucket Sort / Counting Sort

When values are bounded (e.g., 1 to n), use an array as a frequency table instead of a hashmap.

```python
count = [0] * (n + 1)
for x in arr:
    count[x] += 1
# Now count[i] = number of times i appears
```

Use when: values are in a known range, you need O(n) sort, lucky integer, find missing positive.

### Technique E: Computed Hash Key for Grouping

```python
from collections import defaultdict

groups = defaultdict(list)
for word in words:
    key = tuple(sorted(word))   # canonical form
    groups[key].append(word)
return list(groups.values())
```

Use when: group anagrams, group by frequency signature, equal row and column pairs.

## 4. Decision Framework

```
What does the problem ask?

"Does X exist / have I seen X?"
└── Hash set: O(1) lookup

"How many times does X appear?"
└── Counter / frequency map

"Map A values to B values uniquely?"
└── Two hashmaps (bidirectional mapping)

"Group items sharing a property?"
└── Hashmap with computed canonical key

"Values in range [1..n], need O(n)?"
└── Bucket / counting array

"Find missing or extra element?"
├── Small range → set or bucket array
└── Any range → XOR (see Bit Manipulation)
```

## 5. One-Pass vs Multi-Pass Reasoning

Many hashing problems are solved in **one pass** because you build the structure and query it simultaneously:
- "Contains duplicate": add to set, check before adding → one pass
- "Two Sum": store complement → check on arrival → one pass
- "Running sum / prefix sum": compute and store as you go → one pass

**Two passes** are needed when:
- You need the full frequency distribution before making decisions (e.g., "unique number of occurrences" — count first, then check uniqueness of counts)
- You need to know total count before processing (e.g., majority element threshold is n/2, so you need n first)
- You need to query an aggregate of frequencies (e.g., "count elements with maximum frequency" — count first to find the maximum frequency, then sum up occurrences of elements matching that max)

## 6. Index and Pointer Management

Hashing problems rarely involve explicit index manipulation. Key patterns:

- **Enumerate with index**: use `enumerate(arr)` when you need both value and position
- **Two Sum**: store `{value: index}` so you can return the index pair
- **Sliding window + hashmap**: combine with sliding window when the "window" constraint involves frequency (see Sliding Window README)
- **Prefix sum + hashmap**: store `{prefix_sum: first_index}` for subarray sum problems (see Prefix Sum README)

## 7. Complexity Patterns

| Technique | Time | Space |
|---|---|---|
| Hash set membership | O(n) build, O(1) query | O(n) |
| Counter / frequency map | O(n) | O(k) where k = distinct values |
| Bidirectional mapping | O(n) | O(k) |
| Bucket sort | O(n) | O(range) |
| Group by computed key | O(n · key_cost) | O(n) |

Hash operations are O(1) average but O(n) worst case (hash collisions). In practice, treat them as O(1).

## 8. Common Pitfalls

- **Anagram check with different lengths**: always check `len(s) == len(t)` first — Counter comparison will pass for empty strings otherwise
- **Bijection requires two maps**: one map `s→t` is not enough; you also need `t→s` to prevent two source characters mapping to the same target
- **Frequency shape vs frequency equality**: "close strings" requires same key set AND same multiset of values — `Counter(s) == Counter(t)` is too strict; `sorted(Counter(s).values()) == sorted(Counter(t).values())` is the right check
- **Mutating while iterating**: don't modify a dict while iterating over it; collect keys to delete first
- **defaultdict vs dict**: `defaultdict(list)` auto-initializes missing keys; plain `dict` raises `KeyError` — choose based on whether missing keys are expected
- **Integer keys vs string keys**: when using values as keys, be consistent about type (e.g., `str(sorted(word))` vs `tuple(sorted(word))`)
