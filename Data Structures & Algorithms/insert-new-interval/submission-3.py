class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Greeedy
        res = []
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]: # 도착지점이 맨 ~ 뒤라면
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # 다음 인터벌에 들어간다면 
                res.append(intervals[i])
            else: # 오버랩핑 되는 부분
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                    ]
        res.append(newInterval)
        
        return res