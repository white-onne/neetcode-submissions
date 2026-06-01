class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        result = 0
        while left<right:
            minLeft = heights[left]
            minRight = heights[right]
            result = max(result, min(minLeft, minRight)*(right-left))
            if minLeft<minRight:
                left+=1
            else:
                right-=1
        return result