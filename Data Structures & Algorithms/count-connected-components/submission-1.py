class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # 무방향 그래프에서 연결된 요소 갯수 구하기
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # 같은 부모면
            if rank[p2] > rank[p2]:
                par[p1] = p2
                rank[p2]+=rank[p1]
            else:
                par[p2] = p1
                rank[p1]+= rank[p2]
            return 1
        res = n
        for n1,n2 in edges:
            res -= union(n1, n2)
        return res
