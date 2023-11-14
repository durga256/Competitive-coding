# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')   
    def maxPathSum(self, root) -> int: 
        def dfs(root) :
            if root:
                lmax = dfs(root.left)
                rmax = dfs(root.right)                
                curr = root.val
                cmax = max(curr,curr+lmax,curr+rmax,lmax+curr+rmax)
                if cmax > self.ans :
                    self.ans = cmax                
                return max(curr,curr+lmax,curr+rmax)
            else:
                return 0
        dfs(root)
        return self.ans