class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for w in stones:
            heapq.heappush(heap, w*(-1))
        while len(heap)>1:
            a = heapq.heappop(heap)
            a *= -1
            b = heapq.heappop(heap)
            b *= -1
            if a > b:
                heapq.heappush(heap, (a-b)*(-1))
            elif a < b:
                heapq.heappush(heap, (b-a)*(-1))
        if heap:
            return heap[0]*(-1)
        else:
            return 0
                
