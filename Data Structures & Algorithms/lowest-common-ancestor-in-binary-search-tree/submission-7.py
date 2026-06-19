# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        # 문제에서 공통 조상이 있다고 확신해줌
        while cur:
            if cur.val<p.val and cur.val<q.val: # 두 값보다 작으면
                cur = cur.right # 오른쪽에 가장 low 조상이 있을 것
            elif cur.val>p.val and cur.val>q.val: # 두 값보다 크면
                cur = cur.left # 왼쪽에 가장 low 조상이 있을 것
            else:
                break
        return cur