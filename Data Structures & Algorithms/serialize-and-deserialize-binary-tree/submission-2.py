# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        st = []
        def preOrder(cur):
            if not cur:
                st.append("N")
                return
            st.append(str(cur.val))
            preOrder(cur.left)
            preOrder(cur.right)
        preOrder(root)
        
        return ",".join(st)
            

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return  node
        return dfs()
        