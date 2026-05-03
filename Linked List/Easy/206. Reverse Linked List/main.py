# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

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
