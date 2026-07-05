class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_s = s[i:j+1]
                if sub_s==sub_s[::-1] and len(max_str)<len(sub_s):
                       max_str = sub_s
        return max_str