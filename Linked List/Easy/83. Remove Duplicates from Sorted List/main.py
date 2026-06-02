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
