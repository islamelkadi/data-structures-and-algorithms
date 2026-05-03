# LeetCode Organization System — Design

## 1. Current State Analysis

### Existing Folder Structure
```
.
├── 2 Pointers/          ← populated, Easy/Medium/Hard subfolders
├── Arrays & Hashing/    ← populated, Easy/Medium/Hard subfolders
├── Sliding Window/      ← populated, Easy/Medium/Hard subfolders
├── Stack/               ← populated, Easy/Medium/Hard subfolders (no subcategory split)
├── Prefix Sum/          ← partially populated
├── Linked List/         ← partially populated, no difficulty subfolders
├── Bit Manipulation/    ← partially populated
├── Two Pointers/        ← accidentally created, must be deleted
├── questions.md         ← source of truth for all questions
└── organize_questions.py ← scratch script, to be deleted
```

### Current File State
- Most question folders contain only `main.py`
- A small number already have `README.md` (e.g., `125. Valid Palindrome`, `739. Daily Temperatures`)
- Existing READMEs follow a consistent 4-section format — this becomes the canonical template
- `Stack/` has no subcategory split between regular and monotonic stacks
- `Linked List/` has no difficulty subfolders
- Several questions in `questions.md` are not yet placed in any folder

### Existing README Format (canonical — must be preserved)
```markdown
## 1. Algorithm Used
## 2. How to Recognize the Pattern
## 3. Why This Algorithm Fits
## 4. How It Works
```

---

## 2. Target State

### Final Folder Structure
```
.
├── 2 Pointers/
│   ├── README.md                        ← category-level guide
│   ├── Easy/
│   │   ├── 125. Valid Palindrome/
│   │   │   ├── main.py
│   │   │   └── README.md
│   │   └── ...
│   ├── Medium/
│   └── Hard/
│
├── Sliding Window/
│   ├── README.md
│   ├── Easy/
│   ├── Medium/
│   └── Hard/
│
├── Arrays & Hashing/
│   ├── README.md
│   ├── Easy/
│   ├── Medium/
│   └── Hard/
│
├── Stack/
│   ├── README.md
│   ├── Regular/                         ← NEW subcategory
│   │   ├── Easy/
│   │   ├── Medium/
│   │   └── Hard/
│   └── Monotonic/                       ← NEW subcategory
│       ├── Easy/
│       ├── Medium/
│       └── Hard/
│
├── Prefix Sum/
│   ├── README.md
│   ├── Easy/
│   └── Medium/
│
├── Linked List/
│   ├── README.md
│   ├── Easy/                            ← NEW difficulty subfolders
│   └── Medium/
│
├── Bit Manipulation/
│   ├── README.md
│   └── Easy/
│
└── README.md                            ← root algorithmic thinking guide
```

---

## 3. Question-to-Folder Mapping

### 2 Pointers
All questions already in this folder stay. Questions from `questions.md` not yet placed:

| Question | Difficulty | Notes |
|---|---|---|
| 88. Merge Sorted Array | Easy | Same-direction, fill from back |
| 2540. Minimum Common Value | Easy | Converging on two sorted arrays |
| 1679. Max Number of K-Sum Pairs | Medium | Complement pair finding |
| 15. 3Sum | Medium | Already exists in folder |

### Sliding Window
Questions from `questions.md` not yet placed:

| Question | Difficulty | Notes |
|---|---|---|
| 713. Subarray Product Less Than K | Medium | Variable window |
| 2958. Length of Longest Subarray With at Most K Frequency | Medium | Variable window + hashmap |
| 1493. Longest Subarray of 1s After Deleting One Element | Medium | Variable window, k=1 |
| 1004. Max Consecutive Ones III | Medium | Variable window, zero budget |
| 992. Subarrays with K Different Integers | Hard | at-most-k trick |
| 2962. Count Subarrays Where Max Element Appears at Least K Times | Hard | Sliding window counting |
| 1695. Maximum Erasure Value | Medium | Variable window + set |
| 1208. Get Equal Substrings Within Budget | Medium | Variable window, cost constraint |

### Arrays & Hashing
Questions from `questions.md` not yet placed:

| Question | Difficulty | Notes |
|---|---|---|
| 1. Two Sum | Easy | Already in 2 Pointers/Easy — keep there |
| 202. Happy Number | Easy | Hash set cycle detection |
| 1657. Determine if Two Strings Are Close | Medium | Frequency shape comparison |
| 169. Majority Element | Easy | Boyer-Moore voting |
| 1207. Unique Number of Occurrences | Easy | Frequency uniqueness |
| 2215. Find the Difference of Two Arrays | Easy | Set difference |
| 791. Custom Sort String | Medium | Frequency + ordering |
| 2225. Find Players With Zero or One Losses | Medium | Frequency tracking |
| 2244. Minimum Rounds to Complete All Tasks | Medium | Frequency grouping |
| 1426. Counting Elements | Easy | Set membership |
| 1496. Path Crossing | Easy | Coordinate set |
| 13. Roman to Integer | Easy | Hash map lookup |
| 1832. Check if the Sentence Is Pangram | Easy | Set coverage |
| 1941. Check if All Characters Have Equal Number of Occurrences | Easy | Frequency uniqueness |
| 1748. Sum of Unique Elements | Easy | Frequency filter |
| 1512. Number of Good Pairs | Easy | Combination formula |
| 1539. Kth Missing Positive Number | Easy | Set lookup |
| 1394. Find Lucky Integer in an Array | Easy | Frequency match |
| 2053. Kth Distinct String in an Array | Easy | Frequency filter |
| 2085. Count Common Words With One Occurrence | Easy | Frequency intersection |
| 2225. Find Players With Zero or One Losses | Medium | Frequency tracking |
| 2352. Equal Row and Column Pairs | Medium | Tuple hashing |
| 2349. Design a Number Container System | Medium | Bidirectional map |

### Stack — Regular
Questions from `questions.md` not yet placed or to be reorganized:

| Question | Current Location | Difficulty |
|---|---|---|
| 844. Backspace String Compare | not placed | Easy |
| 71. Simplify Path | not placed | Medium |
| 155. Min Stack | Stack/Medium | Medium → move to Regular |
| 150. Evaluate Reverse Polish Notation | Stack/Medium | Medium → move to Regular |
| 394. Decode String | Stack/Medium | Medium → move to Regular |
| 1047. Remove All Adjacent Duplicates In String | not placed | Easy |
| 1544. Make The String Great | not placed | Easy |
| 2390. Removing Stars From a String | not placed | Medium |
| 20. Valid Parentheses | Stack/Easy | Easy → move to Regular |

### Stack — Monotonic
Questions to be reorganized:

| Question | Current Location | Difficulty |
|---|---|---|
| 739. Daily Temperatures | Stack/Medium | Medium → move to Monotonic |
| 853. Car Fleet | Stack/Medium | Medium → move to Monotonic |
| 84. Largest Rectangle in Histogram | Stack/Hard | Hard → move to Monotonic |

### Prefix Sum
Questions from `questions.md` not yet placed:

| Question | Difficulty | Notes |
|---|---|---|
| 724. Find Pivot Index | Easy | Derived suffix |
| 1480. Running Sum of 1d Array | Easy | Basic prefix |
| 1732. Find the Highest Altitude | Easy | Prefix + max |
| 1991. Find the Middle Index in Array | Easy | Same as pivot index |
| 1413. Minimum Value to Get Positive Step by Step Sum | Easy | Prefix min |
| 238. Product of Array Except Self | Medium | Prefix + suffix product |
| 930. Binary Subarrays with Sum | Medium | Prefix + hashmap |
| 1248. Count Number of Nice Subarrays | Medium | Prefix + hashmap |

### Linked List
Questions to add difficulty subfolders:

| Question | Difficulty |
|---|---|
| 83. Remove Duplicates from Sorted List | Easy |
| 206. Reverse Linked List | Easy |
| 876. Middle of the Linked List | Easy |

### Bit Manipulation
| Question | Difficulty |
|---|---|
| 268. Missing Number | Easy |

---

## 4. README Template Design

### Question-Level README (canonical format — matches existing)
```markdown
# {number}. {title}

**Difficulty:** {Easy|Medium|Hard}
**Link:** {leetcode url}

## 1. Algorithm Used

{One sentence naming the specific technique}

## 2. How to Recognize the Pattern

- "{keyword phrase from problem}" → {what it signals} → {technique}.
- {second signal if applicable}
- {third signal if applicable}

## 3. Why This Algorithm Fits

- O(?) time — {reason}.
- O(?) space — {reason}.
- {key property that makes this approach correct}

## 4. How It Works

{2-3 sentence explanation of the core logic}

```python
{minimal code snippet showing the key idea}
```

{1-2 sentences on the key insight or gotcha}
```

### Category-Level README Structure
Each algorithm folder README covers:

```markdown
# {Algorithm Name}

## 1. What It Is
{One paragraph definition}

## 2. When to Use It — Pattern Recognition
### Keywords that signal this algorithm:
- "..." → {what it means}

### Problem characteristics:
- {characteristic 1}
- {characteristic 2}

## 3. Core Technique(s)
### Technique A: {name}
{explanation + minimal code template}

### Technique B: {name}
{explanation + minimal code template}

## 4. Decision Framework
{How to choose between variations}

## 5. One-Pass vs Multi-Pass Reasoning
{When can you solve in a single pass? What makes that possible?}

## 6. Index and Pointer Management
{When to start at 0 vs 1, how to compare to i-th element, ahead/behind}

## 7. Complexity Patterns
{Typical time/space for this category}

## 8. Common Pitfalls
{What goes wrong and how to avoid it}
```

### Root README Structure
```markdown
# Algorithmic Thinking

## 1. How to Read a Problem
## 2. Pattern Recognition Decision Tree
## 3. One-Pass Reasoning — Can This Be Solved in a Single Scan?
## 4. Element Comparison Strategies
   - Comparing element to itself at index i
   - Comparing to element ahead (i+1, i+2)
   - Comparing to element behind (i-1)
   - Comparing from both ends
## 5. Index Management
   - When to start at index 0 vs 1
   - Off-by-one reasoning
   - Boundary conditions
## 6. Constraint-to-Algorithm Mapping
## 7. Complexity Estimation
## 8. Interview Strategy
```

---

## 5. Implementation Approach

### Phase 1: Cleanup
- Delete `Two Pointers/` folder (accidentally created)
- Delete `organize_questions.py` and `algorithm_analysis.md` (scratch files)

### Phase 2: Restructure Stack folder
- Create `Stack/Regular/` and `Stack/Monotonic/` subfolders with Easy/Medium/Hard inside each
- Move existing question folders to correct subcategory
- Remove old flat `Stack/Easy`, `Stack/Medium`, `Stack/Hard` once migrated

### Phase 3: Add missing questions
- Parse `questions.md` to extract code and notes for each question
- Create `main.py` and `README.md` for each question not yet in a folder
- Follow the question-to-folder mapping table in Section 3

### Phase 4: Add missing READMEs to existing questions
- For every question folder that has `main.py` but no `README.md`, generate one
- Use notes from `questions.md` where available; derive from code where not

### Phase 5: Category-level READMEs
- Create `README.md` in each algorithm folder
- Cover all sections defined in the category README template

### Phase 6: Root README
- Create root `README.md` covering the algorithmic thinking framework

---

## 6. Parsing Strategy for questions.md

Each entry in `questions.md` follows this format:
```
---
T: {title or empty}
Q: {url}
A:
```
{code block}
```
---
N:
```
{notes block}
```
---
```

**Parsing rules:**
- `T:` may be empty — if so, derive title from the URL path or problem number
- `A:` block contains the implementation code
- `N:` block contains the notes (may be empty)
- Some entries are missing `T:` entirely — match by URL

**Title resolution for missing T: fields:**
- Extract problem number from URL (e.g., `/problems/container-with-most-water/` → "11. Container With Most Water")
- Cross-reference against existing folder names

---

## 7. Correctness Properties

The following must hold after all tasks are complete:

1. **No duplicate question folders** — each question appears in exactly one location
2. **No orphaned questions** — every question in `questions.md` has a corresponding folder
3. **README consistency** — every question folder contains both `main.py` and `README.md`
4. **Code fidelity** — `main.py` content matches exactly what's in `questions.md`
5. **Stack subcategory correctness** — monotonic stack problems (Daily Temperatures, Car Fleet, Largest Rectangle) are in `Stack/Monotonic/`, not `Stack/Regular/`
6. **No accidental folders** — `Two Pointers/` is removed
7. **Existing READMEs preserved** — the 14 existing README files are not overwritten unless explicitly updating them
