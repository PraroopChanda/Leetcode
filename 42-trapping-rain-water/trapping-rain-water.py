class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        start_pt,last_pt=0, len(height)-1
        leftmax, rightmax=height[start_pt], height[last_pt]
        res=0
        while start_pt<last_pt:
            ## need min(leftmax,rightmax) boundary for computing area
            if leftmax<rightmax: ## right bar is higher so no need to look for it computing area
                start_pt+=1 
                leftmax=max(leftmax,height[start_pt])
                res+=leftmax-height[start_pt] ## no need to check for negatives as leftmax is alread maximum, so min res i can get is 0
            else:
                last_pt-=1
                rightmax=max(rightmax, height[last_pt])
                res+=rightmax-height[last_pt]
            
        return res      