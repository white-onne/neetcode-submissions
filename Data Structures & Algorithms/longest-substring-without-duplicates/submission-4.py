class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        dict = set()
        result = 0
        while right<len(s):
            # 이미 집합에 있으면 left 포인터를 움직여서 그 문자가 집합에 없게 만듦
            if s[right] in dict:
                while s[right] in dict:
                    dict.discard(s[left])
                    left+=1
            dict.add(s[right])
            result = max(result, right-left+1)
            right+=1
        return result