class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        output=[]
        intervals.sort(key=lambda x:x[0])
        curr_start,curr_end=intervals[0]
        for start,end in intervals[1:]:
            if start<=curr_end:
                curr_end=max(end,curr_end)
            else:
                output.append([curr_start,curr_end])
                curr_start,curr_end=start,end
        output.append([curr_start,curr_end])
        return output        
