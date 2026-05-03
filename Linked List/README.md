# Linked List

## 1. What It Is

Linked list problems require manipulating nodes connected by pointers rather than indexed array positions. The key challenge is that you can't jump to an arbitrary position — you must traverse from the head. Most linked list algorithms use one of three approaches: single-pointer traversal (scan and modify), fast/slow pointers (Floyd's algorithm for structural properties), or pointer reversal (in-place restructuring without extra space).

## 2. When to Use It — Pattern Recognition

### Keywords that signal this algorithm:
- "middle of linked list" → fast/slow pointers; slow is at middle when fast reaches end
- "cycle detection" / "has cycle" → fast/slow pointers; they meet iff a cycle exists
- "reverse linked list" / "reverse in groups" → pointer reversal (prev/curr/next)
- "remove duplicates" / "remove nth from end" → single traversal with careful pointer management
- "merge two sorted lists" → two-pointer merge (like merge sort's merge step)
- "palindrome linked list" → find middle (fast/slow), reverse second half, compare

### Problem characteristics:
- Input is a singly or doubly linked list (no random access)
- You need to find a structural property (length, middle, cycle) without extra space
- You need to rearrange nodes in-place
- The problem involves two lists that need to be processed in parallel

## 3. Core Technique(s)

### Technique A: Single Pointer Traversal

Standard scan: follow `curr = curr.next` until `curr` or `curr.next` is `None`.

```python
curr = head
while curr:
    # process curr.val
    curr = curr.next
```

For deletion, maintain a `prev` pointer:

```python
dummy = ListNode(0)
dummy.next = head
prev, curr = dummy, head

while curr:
    if should_delete(curr):
        prev.next = curr.next
    else:
        prev = curr
    curr = curr.next

return dummy.next
```

The **dummy node** before `head` eliminates the special case of deleting the head node.

### Technique B: Fast/Slow Pointers (Floyd's Algorithm)

`slow` moves 1 step per iteration; `fast` moves 2 steps. When `fast` reaches the end, `slow` is at the middle.

```python
# Find middle
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle node
```

For **cycle detection**: if `fast` and `slow` ever point to the same node, there's a cycle.

```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True   # cycle detected
return False
```

For **finding cycle entry point**: after detection, reset one pointer to `head` and advance both one step at a time — they meet at the cycle entry.

### Technique C: Pointer Reversal (In-Place Reverse)

Reverse a linked list by redirecting each node's `next` pointer to its predecessor.

```python
prev = None
curr = head

while curr:
    next_node = curr.next   # save next before overwriting
    curr.next = prev        # reverse the pointer
    prev = curr             # advance prev
    curr = next_node        # advance curr

return prev   # prev is the new head
```

The three-variable pattern (`prev`, `curr`, `next_node`) is the canonical reversal template.

### Technique D: Two-List Merge

Process two lists simultaneously, always taking the smaller head.

```python
dummy = ListNode(0)
curr = dummy

while l1 and l2:
    if l1.val <= l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next

curr.next = l1 or l2   # attach remaining list
return dummy.next
```

## 4. Decision Framework

```
What does the problem ask?

"Find middle / kth from end / split in half"
└── Fast/slow pointers

"Detect or locate a cycle"
└── Fast/slow pointers (Floyd's)

"Reverse the list or a portion of it"
└── Pointer reversal (prev/curr/next)

"Remove a node / remove duplicates / remove nth from end"
└── Single traversal with dummy head + prev pointer

"Merge two sorted lists"
└── Two-pointer merge with dummy head

"Palindrome check"
└── Fast/slow to find middle → reverse second half → compare
```

## 5. One-Pass vs Multi-Pass Reasoning

**Single traversal**: most deletion and modification problems are one pass — maintain enough state (prev, curr) to make decisions locally.

**Fast/slow (middle finding)**: one pass — fast reaches the end exactly when slow reaches the middle.

**Pointer reversal**: one pass — each node is visited exactly once.

**Remove nth from end**: one pass using a gap technique — advance one pointer n steps ahead, then advance both until the lead pointer reaches the end; the trailing pointer is at the node before the target.

```python
dummy = ListNode(0, head)
left, right = dummy, head
for _ in range(n):
    right = right.next
while right:
    left = left.next
    right = right.next
left.next = left.next.next
return dummy.next
```

**Palindrome check**: two passes — first pass finds the middle and reverses the second half; second pass compares the two halves.

## 6. Index and Pointer Management

- **Dummy head node**: use `dummy = ListNode(0); dummy.next = head` whenever you might delete the head or need a stable starting point; return `dummy.next` at the end
- **Loop termination for fast/slow**:
  - `while fast and fast.next` — safe for both even and odd length lists
  - After the loop, `slow` points to the middle (for odd length) or the second of the two middle nodes (for even length)
- **Saving `next` before overwriting**: in pointer reversal, always `next_node = curr.next` before `curr.next = prev` — otherwise you lose the rest of the list
- **Null checks**: always check `node is not None` before accessing `node.next` or `node.val`
- **Reconnecting after reversal**: when reversing only the second half (palindrome check), remember to reconnect the two halves afterward if the list must be restored

## 7. Complexity Patterns

| Technique | Time | Space |
|---|---|---|
| Single traversal | O(n) | O(1) |
| Fast/slow pointers | O(n) | O(1) |
| Pointer reversal | O(n) | O(1) |
| Two-list merge | O(n + m) | O(1) |
| Recursive reversal | O(n) | O(n) call stack |

Linked list algorithms are almost always O(n) time and O(1) space — the in-place pointer manipulation is the whole point.

## 8. Common Pitfalls

- **Losing the rest of the list during reversal**: always save `curr.next` before redirecting `curr.next = prev`
- **Wrong loop condition for fast/slow**: use `while fast and fast.next` — checking only `fast` will crash when `fast.next` is accessed on a null node
- **Off-by-one for "middle"**: for even-length lists, fast/slow gives the second middle node; if you need the first, check `fast.next.next` instead of `fast.next` in the loop condition
- **Forgetting the dummy node**: when deleting the head is possible, always use a dummy node — otherwise you need a special case for head deletion
- **Not restoring the list**: if you reverse the second half for a palindrome check and the problem requires the list to be unchanged afterward, reverse it back before returning
- **Cycle in input**: if the input might have a cycle, a simple `while curr` loop will run forever — use fast/slow to detect cycles first
