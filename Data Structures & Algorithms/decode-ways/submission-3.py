class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if int(s[0])==0:
            return 0
        else: dp[0] = 1

        if len(s)>1:
            if int(s[1])!=0:
                dp[1]=dp[0]
            if int(s[0:2])<=26:
                dp[1]+=1

        for i in range(2, len(s)):
            if int(s[i])!=0: dp[i]=dp[i-1]
            if int(s[i-1:i+1])<=26 and s[i-1]!="0":
                dp[i]+=(dp[i-2])
        return dp[-1]