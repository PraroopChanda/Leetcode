# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next: ## basically fast.next will check for end of linked list
        ## fast.next.next would be null if its the end of linkedin list
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False  