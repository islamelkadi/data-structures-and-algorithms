# 83. Remove Duplicates from Sorted List

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## 1. Algorithm Used

Single pointer traversal that skips duplicate nodes by redirecting `current.next` whenever two consecutive nodes share the same value.

## 2. How to Recognize the Pattern

- "Sorted linked list" + "remove duplicates" → adjacent duplicates only → single pointer is sufficient.
- No need to track previous node separately — you can rewire `current.next` in place.
- In-place modification with no extra space → pointer manipulation, not a new list.

## 3. Why This Algorithm Fits

- O(n) time — each node is visited exactly once.
- O(1) space — no auxiliary data structures; the list is modified in place.
- Sorted order guarantees all duplicates are adjacent, so a single forward pass catches every one.

## 4. How It Works

Start `current` at the head and walk forward. When `current.val == current.next.val`, skip the next node by setting `current.next = current.next.next` — `current` stays put so it can catch runs of three or more duplicates. When the values differ, advance `current` normally. The loop ends when `current` or `current.next` is `None`.

```python
current = head
while current and current.next:
    if current.val == current.next.val:
        current.next = current.next.next
    else:
        current = current.next
return head
```

Not advancing `current` on a duplicate is the critical detail — it lets the same node compare against the next candidate after the skip.
