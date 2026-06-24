import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nPr = itertools.permutations(nums, len(nums))
        ans = []
        for k in nPr:
            lst = []
            for num in k:
                lst.append(num)
            ans.append(lst)
        return ans