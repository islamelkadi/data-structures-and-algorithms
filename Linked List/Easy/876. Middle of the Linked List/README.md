# 876. Middle of the Linked List

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/middle-of-the-linked-list/

## 1. Algorithm Used

Fast/slow pointer (Floyd's tortoise and hare): slow moves 1 step, fast moves 2 steps; when fast reaches the end, slow is at the middle.

## 2. How to Recognize the Pattern

- "Find the middle of a linked list" without knowing the length → two-pointer speed trick → slow/fast pointers.
- No random access on a linked list → can't index to `len // 2` directly → need a traversal-based approach.
- For even-length lists, the problem asks for the second middle node → fast pointer exhausts the list, leaving slow one step past center.

## 3. Why This Algorithm Fits

- O(n) time — single pass through the list.
- O(1) space — only two pointers, no auxiliary storage.
- Avoids a two-pass approach (count length, then walk to `n // 2`) while achieving the same result in one pass.

## 4. How It Works

Start both pointers at head. On each iteration, advance slow by one node and fast by two. When fast is `None` (odd length) or `fast.next` is `None` (even length), the loop exits and slow points to the middle node.

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

For a list of length 5, fast takes 2 full steps (visiting nodes 1→3→5) while slow takes 2 steps (1→2→3), landing exactly at the middle. For length 6, fast takes 3 steps (1→3→5→None via fast.next) and slow lands at node 4 — the second of the two middle nodes, which is what LeetCode expects.

Input: `1 → 2 → 3 → 4 → 5`

| step | slow | fast | fast.next |
|------|------|------|-----------|
| init | 1 | 1 | 2 |
| 1 | 2 | 3 | 4 |
| 2 | 3 | 5 | None → stop |
| result | 3 | | middle node |
