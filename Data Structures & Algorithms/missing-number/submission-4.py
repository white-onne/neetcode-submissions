class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(1, len(nums)+1):
            result = result ^ i ^ nums[i-1]

        return result