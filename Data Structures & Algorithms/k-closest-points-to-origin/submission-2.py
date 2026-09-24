class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(heap, [dist, x, y])
            
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans 