class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        i = 0
        print(nums)
        while i<len(nums):
            if nums[i]>0: break
            target = nums[i]
            left=i+1
            right=len(nums)-1
            while left<len(nums) and right>=0 and left<right:
                if nums[left]+nums[right]+target == 0:
                    ans.add((target, nums[left], nums[right]))
                    # 다음값?
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+target>0:
                    right-=1
                elif nums[left]+nums[right]+target<0:
                    left +=1
            i+=1
        
        return list(ans)