class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s+=str(d)
        result = int(s)+1
        ans = []
        for s in str(result):
            ans.append(int(s))
        return ans