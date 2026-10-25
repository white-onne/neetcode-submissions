# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root):
            if root is None:
                return 0
            return max(get_depth(root.left), get_depth(root.right))+1
        if root is None:
            return True

        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if abs(left_depth-right_depth)>1:
            return False
        
        return True
        