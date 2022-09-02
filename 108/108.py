# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(left,right):
            if left > right:
                return
            cent = (right + left)//2
            node = TreeNode(nums[cent])
            node.left = tree(left,cent - 1)
            node.right = tree(cent+1, right)
            return node
            
        return tree(0,len(nums)-1)

