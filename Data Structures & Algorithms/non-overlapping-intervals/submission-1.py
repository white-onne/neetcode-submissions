class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 시작점 혹은 도착점이 겹치면 오버래핑된 것은 아님
        # 최소갯수의 Intervals를 지워서 non-overlapping되게 만들기 HOW?
        # BruteForce로 풀면 안됨 왜냐하면 시간초과 나버림
        # Greedy로 모든 경우의 수가 맞는지 아닌지 확인한다음에 풀어야 함
        intervals.sort()
        res = 0
        # [start, end]
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd: prevEnd = end # non-Overlapping
            else: # 누구를 지워야 할까요?
                res+=1
                prevEnd = min(end, prevEnd) # 제일 이전에 있는 걸 Take
        
        return res

