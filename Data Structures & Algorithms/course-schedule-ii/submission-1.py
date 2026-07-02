from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 수강할 수 없으면 return []
        # 사이클 있으면 return []
        # 수강할 수 있으면, 전체를 수강할 수 있는 순서를 구해라
        # cycle이 없을 때, 시작 위치는 어디? 즉, 의존 관계가 없는 얘들이 시작 위치이다.
        # (a, b)이면 (b-> a)임으로 a는 의존 관계여서 X
        # 모든 수강 nums을 set에 넣고, 의존 관계, 즉 pre[0]으로 나오는 값은 set에서 뺌
        # 나머지 set에 있는 것들을 시작 위치로 삼으면서 방문
        start = set()
        graph = defaultdict(list)
        for i in range(numCourses):
            start.add(i)
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in start:
                start.remove(prerequisites[i][0])
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        state = [0] * (numCourses)  # 0: unvisit 1:visit 2: done

        def dfs(u):
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1:
                    return True  # cycle 존재
                if state[v] == 0 and dfs(v):
                    return True
            state[u] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0 and dfs(i):
                return []

        ans = []
        for course in start:
            q = deque()
            q.append(course)
            ans.append(course)
            while q:
                node = q.popleft()
                for neigh in graph[node]:
                    q.append(neigh)
                    ans.append(neigh)
        return ans
