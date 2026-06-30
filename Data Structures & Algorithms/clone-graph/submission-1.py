# Definition for a Node.
from collections import deque


# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        create = {1: Node(1)} # 만들어진 노드 목록
        visit = set() # 방문한 노드
        q = deque() # 기존 노드를 저장함
        q.append(node)
        while q:
            node = q.popleft()
 
            if node.val in visit: # 방문한 노드라면
                continue
            # 방문 안한 노드라도 이미 노드가 만들어져 있을것
            # q의 탐색 범위 내에 들었다는 것은 저 아래의 코드를 한번은 거쳤다는 이야기 임으로
            current_node = create[node.val]
            
            visit.add(node.val)
            for neigh in node.neighbors:
                if neigh.val not in create.keys():
                    create[neigh.val] = Node(neigh.val)
                current_node.neighbors.append(create[neigh.val])
                q.append(neigh)
        return create[1]
