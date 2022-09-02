# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.check = True
        self.checktree(root,-inf,inf)
        
        return self.check
    
    def checktree(self, node, low, high):
        if not node: 
            return 
        val = node.val
        if not (low < val < high ):
            self.check = False
            return
        else: 
            self.checktree(node.left,low,val)
            self.checktree(node.right,val,high)
            
        
        
        

