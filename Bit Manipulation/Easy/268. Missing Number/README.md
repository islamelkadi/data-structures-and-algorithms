# 268. Missing Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/missing-number/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Bit Manipulation (XOR summation) or Hash Set (trade space for time).

## 2. How to Recognize the Pattern

- **Find the one missing element in range $[0, n]$**: We are given $n$ distinct numbers in a sequence that should contain $n + 1$ elements.
- **Constant space constraint ($O(1)$ space)**: The problem asks for an $O(1)$ auxiliary space solution, which rules out sets or frequency arrays and signals mathematical/bitwise summation techniques.
- **XOR self-inverse property**: Since $A \oplus A = 0$, XORing every number with its corresponding index leaves only the missing number unpaired.

## 3. Why This Algorithm Fits

- An $O(N)$ space hash set solution is straightforward but violates the $O(1)$ space requirement.
- The XOR-based approach uses a single accumulator variable, checking every index and value in a single pass to achieve $O(N)$ time and $O(1)$ space.

## 4. How It Works

- **Hash Set approach (intuitive but $O(N)$ space)**: Add all array elements to a set, then scan the range from $0$ to $n$ to find which number is missing.
- **XOR approach ($O(1)$ space)**: Initialize `missing = len(nums)` to represent the value $n$. Iterate through `nums` using `enumerate` to XOR each index `i` and element `num` into `missing`. Present elements will cancel themselves out (appearing once as an index and once as a value), leaving only the missing number.

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## READ ME:
        # The problem with the below implementation is that you are storing space in O(n)
        # complexity. This is because you need to create an entry for every item in the
        # range of n. I'm not sure why this is here as it cannot be solved using hash set
        # or hash map and meet the O(1) time complexity.

        # n = len(nums)
        # nums_set = set(nums)
        # n_range = {x for x in range(n+1)}
        # for num in n_range:
        #     if num not in nums_set:
        #         return num

        # Alternative solution:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```

### Dry Run Table (XOR approach)
Input: `nums = [3, 0, 1]` ($n = 3$, expected missing $= 2$)

| i | nums[i] | missing ^= i ^ nums[i] | missing (binary representation) |
|---|---------|------------------------|---------------------------------|
| *init* | — | `missing = 3` | `3` (`011`) |
| 0 | 3 | `3 ^ 0 ^ 3` | `0` (`000`) |
| 1 | 0 | `0 ^ 1 ^ 0` | `1` (`001`) |
| 2 | 1 | `1 ^ 2 ^ 1` | `2` (`010`) |
| **Result** | — | — | **2** |

---

## 5. Time & Space Complexity

### Hash Set Approach
- **Time Complexity**: $O(N)$ to build the set and search the range.
- **Space Complexity**: $O(N)$ to store the array elements in the set.

### XOR Approach
- **Time Complexity**: $O(N)$ to perform a single pass over the array.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a single integer accumulator `missing`.
