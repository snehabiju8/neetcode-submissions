import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-(x-y))
        if len(heap)==1:
            ans=-heapq.heappop(heap)
        else:
            ans=0
        return ans
        
