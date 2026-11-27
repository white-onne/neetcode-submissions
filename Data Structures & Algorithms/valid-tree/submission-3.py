class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for net in adj[node]:
                if net == par:
                    continue
                if not dfs(net, node):
                    return False
            return True
        return dfs(0, -1) and len(visit)==n