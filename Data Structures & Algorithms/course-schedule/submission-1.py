from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # cycle이 생기면 수강 불가능
        # cycle: 아직 탐색 중인 정점을 다시 만나면 cycle
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        state = [0]*(numCourses) # 0: unvisit 1:visit 2: done
        def dfs(u):
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1:
                    return True # cycle 존재
                if state[v] == 0 and dfs(v):
                    return True
            state[u] = 2
            return False
        for i in range(numCourses):
            if state[i] == 0 and dfs(i):
                return False
        return True