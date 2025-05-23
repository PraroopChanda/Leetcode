# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output=[]
        qu=deque([root])
        y=0
        while qu:
            # print(len(qu))
            # output.append(qu[len(qu)-1])
            y=len(qu)-1
            for x in range(len(qu)):
                print(x,len(qu)-1)
                # if x==len(qu)-1:
                #     y=1
                    #print(len(qu)-1)
                curr=qu.popleft()
                #print(curr.val)
                if x==y:
                    output.append(curr.val)
                    #y=0
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
        return output                    