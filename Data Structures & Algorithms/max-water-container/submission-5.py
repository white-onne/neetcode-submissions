class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        ans = 0
        while left<right:
            ans = max(ans, (right-left)*min(heights[left], heights[right]))
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return ans
        