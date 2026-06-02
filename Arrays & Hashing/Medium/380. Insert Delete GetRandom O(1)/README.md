# 380. Insert Delete GetRandom O(1)

**Difficulty:** Medium
**Link:** https://leetcode.com/problems/insert-delete-getrandom-o1/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Hash Map + Dynamic Array combination.

## 2. How to Recognize the Pattern

- **Constant time operations**: The problem requests `insert`, `delete`, and `getRandom` all in $O(1)$ average time.
- **Random selection in constant time**: Generating a random element in $O(1)$ requires a contiguous memory structure like an array/list, where we can index elements directly. Hash sets and hash maps do not support direct random indexing in $O(1)$ time.
- **Constant time search & deletion**: Array deletion at an arbitrary index takes $O(N)$ due to element shifting. To do it in $O(1)$, we need a way to look up the element's index in $O(1)$ (using a hash map) and swap it with the last element of the array before popping it (avoiding shifts).

## 3. Why This Algorithm Fits

- The dynamic array stores the elements and supports $O(1)$ appends and $O(1)$ random indexing.
- The hash map stores `{val: index}` mappings to lookup the index of any value in $O(1)$ time.
- Deletion is optimized to $O(1)$ by copying the last element of the array into the index of the element to delete, updating the hash map with the new index of the moved element, and then popping the last element.

## 4. How It Works

1. **Insert**: Check if the value exists in the hash map. If yes, return `False`. If not, add `val` to the hash map mapping it to the next available index (`len(array)`). Append `val` to the array. Return `True`.
2. **Remove**: Check if the value exists in the hash map. If not, return `False`.
   - Locate the element's index in the array using the hash map: `index = hashmap[val]`.
   - Pop the last element from the array.
   - If the element to delete is not already the last element, copy the popped last element into the array at `index`, and update the hash map mapping for the last element to point to `index`.
   - Delete `val` from the hash map. Return `True`.
3. **GetRandom**: Return a random element from the array using `random.choice(array)`.

```python
import random

class RandomizedSet(object):

    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.hashmap)
        self.array.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False

        index = self.hashmap[val]
        is_last_index = (index == len(self.array) - 1)
        last_element = self.array.pop()
        if not is_last_index:
            self.array[index] = last_element
            self.hashmap[last_element] = index

        del self.hashmap[val]
        return True

    def getRandom(self):
        """
        :type: int
        """
        return random.choice(self.array)
```

### Dry Run Table
Trace of actions: `insert(1)`, `insert(2)`, `remove(1)`, `getRandom()`

| Step | Action | val | array state | hashmap state | Return | Details |
|---|---|---|---|---|---|---|
| *init* | — | — | `[]` | `{}` | — | Initial state |
| 1 | insert | 1 | `[1]` | `{1: 0}` | `True` | 1 is not in hashmap. Append 1, hashmap[1] = 0. |
| 2 | insert | 2 | `[1, 2]` | `{1: 0, 2: 1}` | `True` | 2 is not in hashmap. Append 2, hashmap[2] = 1. |
| 3 | remove | 1 | `[2]` | `{2: 0}` | `True` | 1 is at index 0. Last element is 2. Copy 2 to index 0, update hashmap[2] = 0. Pop 2, delete 1. |
| 4 | getRandom | — | `[2]` | `{2: 0}` | `2` | Returns `2` (the only element). |

---

## 5. Time & Space Complexity

- **Time Complexity**: 
  - **Insert**: $O(1)$ average time for hash map insertion and array append.
  - **Remove**: $O(1)$ average time for hash map lookup/deletion and array pop.
  - **GetRandom**: $O(1)$ time to generate a random index and access the array.
- **Space Complexity**: $O(N)$ auxiliary space to store up to $N$ elements in the array and hash map.
