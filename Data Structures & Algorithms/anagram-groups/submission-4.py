class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary를 통해서 그룹별로 묶는다. 이때 anagram 판별은 걍 문자열 정렬로 한다.
        dict = defaultdict(list)
        ans = []

        for word in strs:
            dict["".join(sorted(word))].append(word)
        for ky in dict.keys():
            ans.append(dict[ky])

        return ans