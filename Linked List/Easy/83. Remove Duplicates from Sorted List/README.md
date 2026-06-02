# 83. Remove Duplicates from Sorted List

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Single pointer traversal that skips duplicate nodes by redirecting `current.next` whenever two consecutive nodes share the same value.

## 2. How to Recognize the Pattern

- **Sorted linked list + remove duplicates**: Since the list is sorted, any duplicate values are guaranteed to be adjacent. Thus, a single forward pointer is sufficient.
- **In-place modification**: Rewiring `current.next` directly avoids allocating new nodes or using auxiliary collections, matching $O(1)$ space.

## 3. Why This Algorithm Fits

- **$O(N)$ time**: Each node is visited exactly once.
- **$O(1)$ space**: No auxiliary data structures are used; the linked list is updated in-place.
- Sorted order guarantees all duplicates are clustered together, so we never need to search backward.

## 4. How It Works

Start `current` at the `head` and walk forward. When `current.val == current.next.val`, skip the next node by setting `current.next = current.next.next`. We do not advance `current` in this step so it can compare against the next node in line (which handles runs of three or more duplicates). When the values differ, advance `current` to `current.next`. The loop ends when `current` or `current.next` becomes `None`.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            # If my current value is equal to that of the NEXT node, then
            # set my current node's next value to point to the node after
            # my current's next node. In the next iteration, this will
            # check if my current node's val is equal to that of my
            # curent node's old next of next node. Essentially, looking
            # one then two nodes ahead.
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Iterate to the next node.
                current = current.next
        return head
```

### Dry Run Table
Input: `1 → 1 → 2 → 3 → 3`

| current | current.next | same val? | action | list state |
|---|---|---|---|---|
| 1 | 1 | yes | skip: `1.next = 2` | `1 → 2 → 3 → 3` |
| 1 | 2 | no | advance | `1 → 2 → 3 → 3` |
| 2 | 3 | no | advance | `1 → 2 → 3 → 3` |
| 3 | 3 | yes | skip: `3.next = None` | `1 → 2 → 3` |
| 3 | None | — | stop | `1 → 2 → 3` |

Result: `1 → 2 → 3`

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of nodes in the linked list. We traverse the list exactly once.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a single traversal pointer (`current`).
