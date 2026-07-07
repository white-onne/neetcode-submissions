class MedianFinder:
    def __init__(self):
        self.minQ = [] # 작은 값들 넣음, 큰 값 추출, - 붙여야 함
        self.maxQ = [] # 큰 값들 넣음, 작은 값 추출

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minQ, -1*num)

        # 항상 minQ<maxQ
        if self.minQ and self.maxQ and (-1*(self.minQ)[0]>self.maxQ[0]):
            val = -1 * heapq.heappop(self.minQ)
            heapq.heappush(self.maxQ, val)

        # minQ와 maxQ 크기 맞추기
        if len(self.minQ) > len(self.maxQ)+1:
            # minQ에 있는 것 한개 maxQ로 이동시키기
            val = -1 * heapq.heappop(self.minQ)
            heapq.heappush(self.maxQ, val)
        elif len(self.minQ) + 1 < len(self.maxQ):
            val = -1 * heapq.heappop(self.maxQ)
            heapq.heappush(self.minQ, val)

    def findMedian(self) -> float:
        if len(self.minQ)>len(self.maxQ):
            return -1*(self.minQ[0])
        elif len(self.minQ)<len(self.maxQ):
            return (self.maxQ[0])
        return (-1*(self.minQ[0]) + self.maxQ[0])/2.0
