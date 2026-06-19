# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(cur, depth):
            if not cur: return
            if len(res)<=depth:
                res.append(cur.val)
            dfs(cur.right, depth+1)
            dfs(cur.left, depth+1)
        dfs(root, 0)        
        return res