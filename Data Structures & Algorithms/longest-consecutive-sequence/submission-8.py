class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        heapq.heapify(nums)
        long_length = 1
        tmp_lenght = 1
        while len(nums)>1:
            num = heapq.heappop(nums)
            print(num)
            if num+1 == nums[0]:
                tmp_lenght+=1
            elif num == nums[0]:
                continue
            else:
                long_length = max(long_length, tmp_lenght)
                tmp_lenght = 1
        long_length = max(long_length, tmp_lenght)
        return long_length