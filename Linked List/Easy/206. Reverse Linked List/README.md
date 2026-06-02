# 206. Reverse Linked List

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/reverse-linked-list/description/

## Table of Contents
1. [1. Algorithm Used](#1-algorithm-used)
2. [2. How to Recognize the Pattern](#2-how-to-recognize-the-pattern)
3. [3. Why This Algorithm Fits](#3-why-this-algorithm-fits)
4. [4. How It Works](#4-how-it-works)
5. [5. Time & Space Complexity](#5-time--space-complexity)

## 1. Algorithm Used

Iterative pointer reversal using three pointers (`previous`, `current`, and `next_node`) to flip each link in a single pass.

## 2. How to Recognize the Pattern

- **Reverse a linked list**: Reorienting a singly-linked list so that the head becomes the tail and vice versa indicates pointer manipulation.
- **In-place reversal constraint**: The problem requires updating the links without allocating new node structures ($O(1)$ auxiliary space), pointing to an iterative approach.

## 3. Why This Algorithm Fits

- The algorithm performs a single pass over the list, yielding $O(N)$ time complexity.
- By adjusting the `next` pointers in-place, the algorithm requires only a few local pointer references ($O(1)$ auxiliary space).

## 4. How It Works

1. Initialize `previous = None` and `current = head`.
2. While `current` is not `None`:
   - Preserve the next node: `next_node = current.next` (otherwise we lose the reference to the rest of the list).
   - Point `current.next` back to `previous` (this reverses the direction of the current link).
   - Update `previous` to be `current`.
   - Update `current` to be `next_node` to advance to the next element.
3. Return `previous` (the final node in the original list, which is the new head of the reversed list).

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous, current = None, head
        while current:
            # 1. Preserve the next node for the final step
            next_node = current.next

            # 2. Set the current's next node to the previous (which essentially reverse it)
            current.next = previous

            # 3. Re-set the previous node for the next iteration
            previous = current

            # 4. Iterate to the next node
            current = next_node

        return previous # Return the last known head, whose next is its previous.
```

### Dry Run Table
Input: `1 → 2 → 3 → 4 → 5 → None`

| step | previous | current | next_node | action |
|------|----------|---------|-----------|--------|
| init | None     | 1       | —         | — |
| 1    | None     | 1       | 2         | `1.next = None`, `prev = 1`, `curr = 2` |
| 2    | 1        | 2       | 3         | `2.next = 1`, `prev = 2`, `curr = 3` |
| 3    | 2        | 3       | 4         | `3.next = 2`, `prev = 3`, `curr = 4` |
| 4    | 3        | 4       | 5         | `4.next = 3`, `prev = 4`, `curr = 5` |
| 5    | 4        | 5       | None      | `5.next = 4`, `prev = 5`, `curr = None` |
| done | 5        | None    | —         | Return `previous` = 5 (`5 → 4 → 3 → 2 → 1 → None`) |

---

## 5. Time & Space Complexity

- **Time Complexity**: $O(N)$ where $N$ is the number of nodes in the linked list. We traverse each node exactly once.
- **Space Complexity**: $O(1)$ auxiliary space as we only use a few pointer variables.
