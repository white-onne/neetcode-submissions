class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result