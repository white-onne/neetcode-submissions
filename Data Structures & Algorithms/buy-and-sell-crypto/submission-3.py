class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_left = [prices[0]]
        max_right = [prices[-1]]
        for i in range(1, len(prices)):
            min_left.append(min(min_left[-1], prices[i]))
        for i in range(len(prices)-1, 0, -1):
            max_right.append(max(max_right[-1], prices[i]))

        for i in range(len(prices)):
            ans = max(ans, max_right[len(prices)-i-1]-min_left[i])
        return ans