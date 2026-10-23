# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == q.val:
            return p
        self.visit = set()
        # 1. p까지 방문
        cur = root
        while True:
            if cur.val == p.val:
                self.visit.add(p.val)
                break
            self.visit.add(cur.val)
            if cur.val<p.val:
                cur = cur.right
            else:
                cur = cur.left
        self.result = None
        print(self.visit)
        self.dfs(root, q.val)
        result = self.result
        return result

    def dfs(self, cur, val):
        if cur.val == val:
            if cur.val in self.visit and not self.result:
                self.result = cur
            return None
        if cur.val < val:
            self.dfs(cur.right, val)
        else:
            self.dfs(cur.left, val)

        if cur.val in self.visit and not self.result:
            self.result = cur
        return None