class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0 for x in range(len(height))]
        max_right=[0 for x in range(len(height))]
        min_lr=[0 for x in range(len(height))]
        length=len(height)-1
        area=0
        for x in range(len(height)):
            if x==0:
                continue
            if height[x-1]>max_left[x-1]: ## left to right pass
                max_left[x]=height[x-1]
            else:
                max_left[x]=max_left[x-1]
            if height[length-x+1]>max_right[length-x+1]: ## right to left pass
                max_right[length-x]=height[length-x+1]
            else:
                max_right[length-x]=max_right[length-x+1]
        for y in range(len(height)):
            min_lr[y]=min(max_left[y],max_right[y])
            if min_lr[y]-height[y]>0:
                area+=min_lr[y]-height[y]
        return(area)
        