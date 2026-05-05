# 206. Reverse Linked List

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-linked-list/

## 1. Algorithm Used

Iterative pointer reversal using three variables — `previous`, `current`, and `next_node` — to flip each link in a single pass.

## 2. How to Recognize the Pattern

- "Reverse a linked list" → classic pointer reversal → track previous and current simultaneously.
- In-place requirement with O(1) space → iterative approach over recursive.
- No random access needed → a single forward scan with local pointer swaps is enough.

## 3. Why This Algorithm Fits

- O(n) time — every node is visited exactly once.
- O(1) space — only three pointer variables regardless of list length.
- Each iteration reverses exactly one link, so the invariant is simple to reason about and verify.

## 4. How It Works

Initialize `previous = None` and `current = head`. On each iteration, save `current.next` before overwriting it, point `current.next` back to `previous`, then advance both pointers one step forward. When `current` reaches `None`, `previous` is sitting on the new head of the reversed list.

```python
previous, current = None, head
while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
return previous
```

Saving `next_node` before the reversal is essential — once `current.next` is overwritten, the rest of the original list would be unreachable without it.

Input: `1 → 2 → 3 → 4 → 5`

| step | previous | current | next_node | action |
|------|----------|---------|-----------|--------|
| init | None | 1 | — | |
| 1 | None | 1 | 2 | 1.next=None, prev=1, curr=2 |
| 2 | 1 | 2 | 3 | 2.next=1, prev=2, curr=3 |
| 3 | 2 | 3 | 4 | 3.next=2, prev=3, curr=4 |
| 4 | 3 | 4 | 5 | 4.next=3, prev=4, curr=5 |
| 5 | 4 | 5 | None | 5.next=4, prev=5, curr=None |
| done | 5 | None | — | return 5 → 4 → 3 → 2 → 1 |
