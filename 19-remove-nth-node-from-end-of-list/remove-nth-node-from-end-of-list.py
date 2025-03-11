# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## doing with 2 pointer
        dummy=ListNode(0,head)
        first=head
        second=dummy ## this will help me in the edge case when its just 1
        if head.val == None: ## edge case
            return head
        for i in range(n):
            first=first.next
        ## now iterating both
        ## right now they exactly have a gap of n nodes
        while first: 
            first=first.next
            second=second.next
        ## now removing the node
        second.next=second.next.next ## This will help in the edge case as second is dummy this time

        return dummy.next   