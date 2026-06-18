# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        if not root:
            return True

        
        if not self.isBalanced(root.left): return False
        if not self.isBalanced(root.right): return False
        
        left_depth = self.maxHeights(root.left)
        right_depth = self.maxHeights(root.right)
        
        if abs(left_depth-right_depth) > 1:
            return False
        return True

    def maxHeights(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxHeights(root.left), self.maxHeights(root.right))