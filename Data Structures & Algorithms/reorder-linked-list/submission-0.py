# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow.next
        slow.next=None
        while current is not None:
            nexts=current.next
            current.next=prev
            prev=current
            current=nexts
        start=head
        while prev is not None:
            start_next=start.next
            prev_next=prev.next
            start.next=prev
            prev.next=start_next
            start=start_next
            prev=prev_next