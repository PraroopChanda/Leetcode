# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        ## reversing the second linked list
        prev=None
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node
        
        ## now prev is the reversed linked list and now merging both
        second=prev
        first=head
        ## now merging both
        while second: ## as second would be equal or shorter to first
            tmp1,tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

        




