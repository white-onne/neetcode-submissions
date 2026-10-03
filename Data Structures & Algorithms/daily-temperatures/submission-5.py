class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                old_idx = stack.pop()
                ans[old_idx] = i-old_idx
            stack.append(i)

        return ans
