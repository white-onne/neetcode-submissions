class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_dict = {}
        for i in range(26):
            alpha_dict[i] = 0

        for chr in s:
            alpha_dict[ord(chr)-97] += 1
        for chr in t:
            alpha_dict[ord(chr)-97] -= 1
        for k in alpha_dict.keys():
            if alpha_dict[k] != 0:
                return False
        return True

