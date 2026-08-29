class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for st in strs:
            ch = [0]*26
            for c in st:
                ch[ord(c)-ord('a')]+=1
            
            dict[tuple(ch)].append(st)
        ans = []
        for key in dict.keys():
            ans.append(list(dict[key]))
        return ans