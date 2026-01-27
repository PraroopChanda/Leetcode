class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        output=[]
        st_start=newInterval[0]
        st_end=newInterval[1]
        count=0

        for start,end in intervals:
            count+=1
            if end<st_start:
                output.append([start,end])  
            elif st_end>=start:
                st_end=max(st_end,end)
                st_start=min(st_start,start)
            else:
                output.append([st_start,st_end])
                st_start,st_end=start,end
        output.append([st_start,st_end])        
                
        return output
                




        