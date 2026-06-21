# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path들의 sum이 제일 큰걸 return, -값도 있고 +값도 있음
        # greedy 쓰면 될듯
        # 노드를 탐색함 위로 올라가면서 max값을 계속 갱신해줌
        # 만약 이전값이 -라면 0과 다름없음으로 0으로 초기화 하고 나로 초기화 한다. 그리고 나서 max값 갱신
        # 문제는 left, right 중 큰 값을 선택해야 한다는 것. 두개다 포함하면 올바른 path가 아님
        # 근데 내 노드에서는 left+right+me vs max 해도 됨
        # 그런데 위로 올리는 값은 left+me vs right+me임
        # 그런데 위로 올릴 때 저 둘중에 값이 -인게 있으면 걍 나만 올림 왜냐하면 -에 누구를 더하든간에 값이 작기 때문
        # 카데인과 그래프
        self.ans = root.val
        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            
            left = max(0, left)
            right = max(0, right)

            self.ans = max(left+right+cur.val, self.ans)
            # 음수면 0과 다름없다
            
            return max(left, right)+cur.val
        dfs(root)
        
        return self.ans