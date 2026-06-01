class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0]*len(height)
        pre[0] = height[0]
        post = [0]*len(height)
        post[-1] = height[-1]
        for i in range(1, len(height)):
            pre[i] = max(pre[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            post[i] = max(post[i+1], height[i+1])
        result = 0
        for i in range(len(height)):
            result+=max(0, min(pre[i], post[i])-height[i])
        return result    