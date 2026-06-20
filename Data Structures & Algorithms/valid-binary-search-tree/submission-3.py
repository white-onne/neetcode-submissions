# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur, left, right): # -1000<=val<=1000
            if not cur:
                return True
            # 아오 피곤해
            # 오른쪽에서 온 값이라면 prevVal보다 커야 하고, 특정 값보단 작아야 함
            if not (cur.val<right and cur.val>left):
                return False
                # 왼쪽으로 가면 내 부모 노드보다 값이 더 작아야 함 그래서 부모 노드가 right bound
                # 오른쪽으로 가면 내 부모 노드보다 값이 더 커야 함 그래서 부모 노드가 left bound
            return dfs(cur.left, left, cur.val) and dfs(cur.right, cur.val, right)
        

        return dfs(root, -1001, 1001)