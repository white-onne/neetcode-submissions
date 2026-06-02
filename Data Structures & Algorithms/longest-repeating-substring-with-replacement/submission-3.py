class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) # 문자와 문자 등장 횟수 # 어차피 상수개임 26개
        left, right = 0, 0
        result = 0
        while left<=right and right<len(s):
            count[s[right]]+=1
            # k갯수로 커버 가능한지 알아야 함
            # get most max cnt
            # get duplication list
            maxcnt = 0
            for ky in count.keys():
                maxcnt = max(maxcnt, count[ky])
            if right-left+1-maxcnt>k:
                count[s[left]]-=1
                left+=1
            else:
                result = max(result, right-left+1)
            right+=1
        return result
