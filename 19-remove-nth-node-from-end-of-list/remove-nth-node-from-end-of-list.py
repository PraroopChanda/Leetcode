# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## putting everything in a list and then doing
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        remove_index=len(nodes)-n
        if remove_index==0:
            return head.next
        nodes[remove_index-1].next=nodes[remove_index].next ## skipping the connection in between
        return head