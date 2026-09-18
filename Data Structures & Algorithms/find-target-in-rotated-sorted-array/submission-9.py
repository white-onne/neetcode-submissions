class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l + r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l

        left, right = 0, len(nums)-1
        
        if target>=nums[pivot] and target<=nums[right]:
            left = pivot
        else:
            right = pivot-1

        while left<=right:
            m = (left+right)//2
            if nums[m] == target:
                return m
            elif nums[m]<target: # 오른쪽
                left = m + 1
            else:
                right = m - 1
        return -1
        