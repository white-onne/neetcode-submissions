class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.topk = k
        for num in nums:
            heapq.heappush(self.heap, num)
        while self.heap and len(self.heap)>self.topk:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        while self.heap and len(self.heap)>self.topk:
            heapq.heappop(self.heap)

        return self.heap[0]
        
