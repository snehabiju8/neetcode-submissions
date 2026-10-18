class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in hashed:
                hashed[key]=[]
            hashed[key].append(i)
        output=[]
        for i in hashed:
            output.append(hashed[i])
        return output
        