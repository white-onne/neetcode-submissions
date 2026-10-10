class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        def dfs(start_idx: int, current_target: int, current_arr: list[int]):
            if current_target<0:
                return
            if current_target==0:
                subset.append(current_arr.copy())
                return
            for i in range(start_idx, len(nums)):
                current_arr.append(nums[i])
                dfs(i, current_target-nums[i],current_arr)
                current_arr.pop()
        dfs(0, target, [])
        return subset