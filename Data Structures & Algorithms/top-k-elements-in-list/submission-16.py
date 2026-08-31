import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for ky in cnt.keys():
            heapq.heappush(heap, (cnt[ky], ky))
        while heap and len(heap)>k:
            heapq.heappop(heap)
        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result