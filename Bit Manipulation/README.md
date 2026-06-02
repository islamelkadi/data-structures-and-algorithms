# Bit Manipulation


## Table of Contents
1. [1. What It Is](#1-what-it-is)
2. [2. When to Use It — Pattern Recognition](#2-when-to-use-it--pattern-recognition)
   - [Keywords that signal this algorithm:](#keywords-that-signal-this-algorithm)
   - [Problem characteristics:](#problem-characteristics)
3. [3. Core Technique(s)](#3-core-techniques)
   - [Technique A: XOR Pairing — Find the Unique Element](#technique-a-xor-pairing--find-the-unique-element)
   - [Technique B: XOR Pairing — Find the Missing Number](#technique-b-xor-pairing--find-the-missing-number)
   - [Technique C: Bit Masking — Check and Set Bits](#technique-c-bit-masking--check-and-set-bits)
   - [Technique D: Shift Operations](#technique-d-shift-operations)
   - [Technique E: Count Set Bits (Brian Kernighan)](#technique-e-count-set-bits-brian-kernighan)
4. [4. Decision Framework](#4-decision-framework)
5. [5. One-Pass vs Multi-Pass Reasoning](#5-one-pass-vs-multi-pass-reasoning)
6. [6. Index and Pointer Management](#6-index-and-pointer-management)
7. [7. Complexity Patterns](#7-complexity-patterns)
8. [8. Common Pitfalls](#8-common-pitfalls)

## 1. What It Is

Bit manipulation solves problems by operating directly on the binary representation of integers. Instead of using loops or hash structures, you exploit properties of bitwise operators (XOR, AND, OR, shifts) to achieve O(1) or O(n) solutions with O(1) space. The most powerful property is XOR: it cancels paired values and isolates unpaired ones, making it ideal for "find the missing/unique element" problems.

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "missing number" / "find the missing integer" → XOR pairing (index XOR value)
- "single number" / "element that appears once" → XOR all elements; pairs cancel
- "power of two" → `n & (n - 1) == 0` (exactly one bit set)
- "count set bits" / "number of 1s in binary" → Brian Kernighan's algorithm or `bin(n).count('1')`
- "swap without temp variable" → XOR swap
- "subset" / "bitmask" → use integer bits to represent inclusion/exclusion
- "divide by 2" / "multiply by 2" → right shift `>> 1` / left shift `<< 1`

### Problem characteristics:
- Elements appear in pairs except for one (or two) outliers
- You need O(1) space and the hash set approach feels wasteful
- The problem involves binary properties (even/odd, powers of two, bit counts)
- You need to represent a set of boolean flags compactly

## 3. Core Technique(s)

### Technique A: XOR Pairing — Find the Unique Element

XOR properties that make this work:
- `a ^ a = 0` — a value XORed with itself cancels out
- `a ^ 0 = a` — XOR with zero is identity
- XOR is commutative and associative — order doesn't matter

```python
# Single Number: one element appears once, all others appear twice
result = 0
for x in arr:
    result ^= x
return result   # all pairs cancel; result is the unique element
```

### Technique B: XOR Pairing — Find the Missing Number

XOR every index (0 to n) with every value. Paired index-value combinations cancel; the unpaired index is the missing number.

```python
def missing_number(nums):
    result = len(nums)   # start with n (the "extra" index)
    for i, x in enumerate(nums):
        result ^= i ^ x
    return result
```

Why it works: you're XORing `0 ^ 1 ^ 2 ^ ... ^ n` (all indices including n) with `nums[0] ^ nums[1] ^ ... ^ nums[n-1]` (all values). Every number that appears in both cancels; the missing number appears only once.

Alternative using sum: `missing = n*(n+1)//2 - sum(nums)` — simpler but can overflow for large n.

### Technique C: Bit Masking — Check and Set Bits

```python
# Check if bit k is set
(n >> k) & 1 == 1

# Set bit k
n | (1 << k)

# Clear bit k
n & ~(1 << k)

# Toggle bit k
n ^ (1 << k)

# Check if n is a power of two (exactly one bit set)
n > 0 and (n & (n - 1)) == 0

# Get the lowest set bit
n & (-n)

# Clear the lowest set bit
n & (n - 1)
```

### Technique D: Shift Operations

```python
# Multiply by 2^k
n << k

# Integer divide by 2^k (arithmetic right shift)
n >> k

# Check if n is even
n & 1 == 0

# Check if n is odd
n & 1 == 1
```

### Technique E: Count Set Bits (Brian Kernighan)

```python
def count_bits(n):
    count = 0
    while n:
        n &= n - 1   # clears the lowest set bit
        count += 1
    return count
```

Each iteration removes exactly one set bit, so this runs in O(number of set bits) rather than O(32).

## 4. Decision Framework

```
"Find the one element that appears once (all others appear twice)"
└── XOR all elements: pairs cancel, unique survives

"Find the missing number in [0..n]"
└── XOR all indices 0..n with all values; or use sum formula

"Is n a power of two?"
└── n > 0 and (n & (n-1)) == 0

"Count the number of 1-bits"
└── Brian Kernighan: n &= n-1 in a loop; or bin(n).count('1')

"Represent a subset / combination of flags"
└── Bitmask: bit k = 1 means element k is included

"Two elements appear once, all others appear twice"
└── XOR all → get a^b; find any set bit; partition array by that bit; XOR each partition
```

## 5. One-Pass vs Multi-Pass Reasoning

XOR-based solutions are **one pass**: scan the array once, XOR each element into the accumulator. No preprocessing or second pass needed.

The reason one pass works: XOR is associative and commutative, so the order of operations doesn't matter. You're effectively computing the XOR of all elements simultaneously, and the algebraic properties guarantee the result.

Bit counting (Brian Kernighan) is O(k) where k is the number of set bits — not a pass over an array, but a loop over the bits of a single number.

## 6. Index and Pointer Management

Bit manipulation problems rarely involve array indices in the traditional sense. Key patterns:

- **XOR pairing with indices**: `enumerate(nums)` gives you both `i` and `nums[i]` to XOR together
- **Bitmask iteration**: to iterate over all subsets of an n-element set, loop `mask` from `0` to `2^n - 1`; check if element `k` is in the subset with `(mask >> k) & 1`
- **Bit position**: bit 0 is the least significant (rightmost); bit k has value `2^k`

```python
# Iterate over all subsets
for mask in range(1 << n):
    subset = [arr[k] for k in range(n) if (mask >> k) & 1]
```

## 7. Complexity Patterns

| Technique | Time | Space |
|---|---|---|
| XOR all elements (single number) | O(n) | O(1) |
| XOR pairing (missing number) | O(n) | O(1) |
| Power of two check | O(1) | O(1) |
| Count set bits (Brian Kernighan) | O(k), k = set bits | O(1) |
| Bitmask subset enumeration | O(2^n · n) | O(1) |

The O(1) space is the main advantage over hash-based approaches for pairing problems.

## 8. Common Pitfalls

- **XOR is not addition**: `a ^ b` is not `a + b`; XOR cancels identical bits, it doesn't sum them
- **Missing number with XOR**: you must XOR indices 0 through n (inclusive), not 0 through n-1 — the "extra" index n is what makes the missing number unpaired
- **Power of two edge case**: `n = 0` satisfies `n & (n-1) == 0` but is not a power of two — always add `n > 0` to the check
- **Signed integer right shift**: in Python, `>>` is arithmetic (sign-extending); in other languages, behavior on negative numbers may differ
- **Integer overflow**: Python integers are arbitrary precision, so overflow isn't an issue; in Java/C++, use `long` for large XOR accumulations
- **Two unique numbers**: if two elements appear once and all others appear twice, a single XOR gives `a ^ b` — you need an extra step (find a set bit in `a ^ b`, partition the array by that bit, XOR each partition separately) to isolate `a` and `b`
