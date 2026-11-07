from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        state = [0]*(numCourses)
        def dfs(u):
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1:
                    return True
                if state[v] == 0 and dfs(v):
                    return True
            state[u] = 2
            return False
        for i in range(numCourses):
            if state[i] == 0 and dfs(i):
                return False
        return True