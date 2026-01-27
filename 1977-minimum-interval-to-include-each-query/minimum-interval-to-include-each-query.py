class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap=[]

        res,i={},0 ## res is basically the result, i is the iterator
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q: ## first adding the elements which have starting less than the query
                l,r=intervals[i]
                heapq.heappush(min_heap,(r-l+1,r))
                i+=1 ## going to next element in the list, if for the  next element, it is inside the previous range, it would automatically be covered no need to go back
            ## next cleaning any invalid parts
            while min_heap and min_heap[0][1]<q:
                heapq.heappop(min_heap)
            ## now assign the value
            res[q]=min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]

                
                    

        