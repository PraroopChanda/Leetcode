# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## Doing a 2 pass thing, getting the length and doing it
        ## space is complexity remains O(1)
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        remove_index=length-n
        if remove_index==0:
            return head.next
        curr=head
        idx=0
        while curr:
            if remove_index-1==idx:
                curr.next=curr.next.next
                break
            curr=curr.next
            idx+=1
        return head  