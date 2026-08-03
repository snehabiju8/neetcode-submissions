class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1=sorted(s)
        res2=sorted(t)
        return res1==res2