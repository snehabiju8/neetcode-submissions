class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        new=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            new.append(sorted_items[i][0])
        return new

        