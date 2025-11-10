class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist_0(x,y):
            return (x**2 + y**2) **0.5
        output=[]    
        dist_list=[]
        for point in points:
            dist_list.append((dist_0(point[0],point[1]),point))
        heapq.heapify(dist_list)
        for num in range(k):
            output.append(heapq.heappop(dist_list)[1])
        return output    



        