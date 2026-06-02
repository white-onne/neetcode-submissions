class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = [0] * len(prices)
        maxVal[len(prices)-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxVal[i] = max(maxVal[i+1], prices[i+1])
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, maxVal[i]-prices[i])
        return max(0, ans)