# 202. Happy Number
**Difficulty:** Easy
**Link:** https://leetcode.com/problems/happy-number/

## 1. Algorithm Used

Hash set cycle detection applied to the digit-square-sum sequence.

## 2. How to Recognize the Pattern

- "detect if a process loops forever" → need to track visited states → hash set.
- The sequence either reaches 1 (happy) or enters a cycle (not happy).
- Finite state space means a cycle must eventually occur if 1 is never reached.

## 3. Why This Algorithm Fits

- O(log n) per step — each iteration reduces n to the sum of squared digits, which is much smaller.
- O(k) space — k is the number of unique values seen before a cycle or termination.
- A set gives O(1) membership checks, making cycle detection straightforward.

## 4. How It Works

Repeatedly replace n with the sum of the squares of its digits. Before each replacement, check if n is already in the seen set — if so, a cycle exists and the number is not happy. If n reaches 1, return True.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return True
```

The key insight is that any non-happy number will eventually cycle back to a previously seen value, so a set is all you need to detect that.
