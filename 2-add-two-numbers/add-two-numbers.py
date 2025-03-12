# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        curr=dummy
        carry=0

        while l1 or l2 or carry: ## add carry for the edge case
            val1=l1.val if l1 else 0 ## basically if its null just add 0
            val2=l2.val if l2 else 0

            sum1=val1+val2+carry ## adding carry here, should cover the edge case 9+9 for example
            carry=sum1//10
            val=sum1%10
            curr.next=ListNode(val)

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            curr=curr.next

        return dummy.next          