# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if bool(p)!=bool(q):
            return False    
        queuep=deque([p])
        queueq=deque([q])
        while queuep and queueq:
            currp=queuep.popleft()
            currq=queueq.popleft()
            if (currp.val!=currq.val) or (bool(currp.left)!=bool(currq.left)) or (bool(currp.right)!=bool(currq.right)):               
                return False
            if currp.left:
                queuep.append(currp.left)
            if currq.left:
                queueq.append(currq.left)
            if currp.right:
                queuep.append(currp.right)
            if currq.right:
                queueq.append(currq.right) 
        return True            
        