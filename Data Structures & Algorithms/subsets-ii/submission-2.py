class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur_idx, cur_arr):
            if cur_idx == len(nums):
                res.append(cur_arr.copy())
                return
            cur_arr.append(nums[cur_idx])
            dfs(cur_idx + 1, cur_arr)
            cur_arr.pop()

            while cur_idx + 1 < len(nums) and nums[cur_idx] == nums[cur_idx+1]:
                cur_idx += 1
            dfs(cur_idx + 1, cur_arr)

        dfs(0, [])
        return res