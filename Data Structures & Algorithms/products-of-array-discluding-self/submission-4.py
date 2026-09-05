class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1] * len(nums)
        for i in range(1, len(nums)):
            l.append(l[-1]*nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1]*nums[i+1]
        ans = []
        for i in range(len(nums)):
            ans.append(l[i]*r[i])
        return ans