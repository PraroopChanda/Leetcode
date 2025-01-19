class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start_pt, end_pt=0, len(heights)-1
        max_area=0
        while start_pt<end_pt:
            area=(end_pt-start_pt)*min(heights[start_pt],heights[end_pt]) ## get the area
            if area>max_area:
                max_area=area
            if heights[start_pt]<heights[end_pt]: ## because lower bar forms the height of rectangle
                start_pt+=1
            else:
                end_pt-=1

        return max_area   