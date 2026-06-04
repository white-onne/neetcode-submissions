class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair( idx, height ) height를 적용할 수 있는 시작 인덱스와 height 저장
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))
        # stack에 남아있는 값들
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea