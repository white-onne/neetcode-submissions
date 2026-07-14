import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        re_s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()
        start, end = 0, len(re_s)-1
        while start<end: # 0, 1
            if re_s[start] != re_s[end]:
                return False
            start += 1
            end -= 1
        return True
