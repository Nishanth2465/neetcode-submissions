# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        benni=[]
        curr=[]
        q=deque([root])
        while q:
            answer=None
            lin=len(q)

            for i in range(lin):
                curr=q.popleft()
                if curr:
                    answer=curr
                    q.append(curr.left)
                    q.append(curr.right)
            if answer:
                benni.append(answer.val)
        return benni
        
                
            



      
            
            
             
            
        