class MedianFinder:

    def __init__(self):
        self.max_heap=[] ## left half 
        self.min_heap=[] ## right half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        ### check for values--> left should be small and right should be max
        if self.max_heap and self.min_heap and (-self.max_heap[0]>self.min_heap[0]):
            val=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)
        ## now length
        if len(self.max_heap)>len(self.min_heap)+1:
            val=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>len(self.max_heap)+1:
            val=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)

    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return ((-self.max_heap[0]+self.min_heap[0])/2)
        elif len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]    
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()