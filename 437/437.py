# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # Can remove sums[currSum-targetSum] prefixSums to get target
                count = sums[total-targetSum]

                # Add value of this prefixSum
                sums[total] += 1
                # Explore children
                count += dfs(root.left, total) + dfs(root.right, total)
                # Remove value of this prefixSum (path's been explored)
                sums[total] -= 1

            return count

        return dfs(root, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ------------------------------------
#         self.res = 0
#         self.target = targetSum
#         if self.target == 0:
#             return(str(root).count("0"))
        
#         self.check(root)
#         self.bfs(root)
#         return self.res
    
#     def bfs(self,root):
#         if not root: 
#             return 
#         else:
#             val = root.val
#             self.check(root.left,val)
#             self.check(root.right,val)
#             self.bfs(root.left)
#             self.bfs(root.right)

#     def check(self,root,val= ):
#         if not root: return
#         val += root.val
#         print(val)
        
#         if val > self.target:
#             val = None
#             self.check(root.right,val)
#             self.check(root.left,val)
#         if val == self.target:
#             self.res += 1
#             val = None
            
#         self.check(root.right,val)
#         self.check(root.left,val)
        
        
        
