class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict1={}
        for n in range(len(position)):
            if position[n] not in dict1:
                dict1[position[n]]=speed[n]
        position.sort(reverse=True)
        count=0
        last_time=0
        for n in range(len(position)):
            ans=(target-position[n])/dict1[position[n]]
            if ans>last_time:
                count+=1
                last_time=ans
        return count