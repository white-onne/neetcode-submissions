import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Priority Queue
        ans = []
        count_dict = Counter(nums)
        top_k = []
        
        for ky in count_dict.keys():
            heapq.heappush(top_k, (-count_dict[ky], ky))
        
        for i in range(k):
            cnt, val = heapq.heappop(top_k)
            ans.append(val)
        
        return ans
        

