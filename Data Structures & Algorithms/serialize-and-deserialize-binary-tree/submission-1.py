# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # PreOrder로 string으로 만들어줌
        # PreOrder와 NULL표식가지고만으로 serial, decode가 가능함
        # root => left => right
        # N은 노드의 마지막(NULL)을 의미할 것임
        st = [] # str이 아닌 이유는 ,을 기준으로 노드가 구분되기 때문
        def preOrder(cur):
            if not cur:
                st.append("N")
                return
            st.append(str(cur.val))
            preOrder(cur.left)
            preOrder(cur.right)
        preOrder(root)
        
        return ",".join(st)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            # preOrder에게 맞긴다(root => left => right)
            node.left = dfs()
            node.right = dfs()
            return  node
        return dfs()
        