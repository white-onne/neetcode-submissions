class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums)>1:
            return False
        q = [0] # 도달할 수 있는 인덱스 저장
        visit = [False] * len(nums)
        visit[0] = True
        while q:
            idx = q.pop()
            can_jump = nums[idx]
            for k in range(idx, min(idx+can_jump+1,len(nums))):
                if k!=len(nums)-1 and nums[k]==0: continue
                if visit[k]: continue
                q.append(k)
                visit[k] = True

        return visit[-1]