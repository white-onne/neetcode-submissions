# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level 별 탐색
        # 왼쪽에서 오른쪽으로 탐색
        if not root: return []
        self.ans = []
        def dfs(cur, depth):
            if not cur: return
            if len(self.ans)<depth:
                self.ans.append([cur.val])
            else:
                self.ans[depth-1].append(cur.val)
            dfs(cur.left, depth+1)
            dfs(cur.right, depth+1)
        dfs(root, 1)
        return self.ans