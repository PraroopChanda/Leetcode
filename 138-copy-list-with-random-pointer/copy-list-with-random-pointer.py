"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict_1={None:None} ## edge case when random points to None
        curr=head
        ## done with one pass of the linked list
        while curr:
            new_node=Node(curr.val)
            dict_1[curr]=new_node
            curr=curr.next
        ## node creation
        curr=head
        while curr:
            dict_1[curr].next=dict_1[curr.next] ## this mapping is creating a deep copy as it is linking 
            ## separate elements in the dictionary
            dict_1[curr].random=dict_1[curr.random]    
            curr=curr.next
        return dict_1[head]    

        