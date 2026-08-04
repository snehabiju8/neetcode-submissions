class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        lef_max,righ_max=0,0
        for i in range(len(height)):
            lef_max=max(lef_max,height[i])
            leftmax[i]=lef_max
        for i in range(len(height)-1,-1,-1):
            righ_max=max(righ_max,height[i])
            rightmax[i]=righ_max
        water=0
        for i in range(len(height)):
            wat=min(leftmax[i],rightmax[i])-height[i]
            water+=wat
        return water
        
            
        