class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        len_nums = len(nums)
        def backtracking(start_idx:int, current_arr:list):
            if start_idx>=len_nums:
                return
            new_arr = list(current_arr)
            for i in range(start_idx, len_nums):
                new_arr.append(nums[i])
                subset.append(list(new_arr))
                backtracking(i+1, list(new_arr))
                new_arr.pop()
            return

        backtracking(0, [])
        return subset