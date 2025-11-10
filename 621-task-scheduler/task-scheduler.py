class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_1=Counter(tasks) ## basically a hash map for frequency of elements
        max_heap=[-cnt for cnt in dict_1.values()] # --> building a maxheap
        heapq.heapify(max_heap) ## (O(nlogn) --> n can be max 26)

        queue=deque() ## queue for FIFO, deque for popping from left and right
        time=0

        '''
        LOGIC 
        ** basically we always try to execute the most frequent element first (greedy --> optimal solution) --> max heap gives that
        ** Next, we take it out, and put the remaining in a queue with a TIME when it can be executed again (time + n)
        ** Next, if its time, we push it back to max_heap and exectute
        '''

        while max_heap or queue:
            time+=1
            if max_heap:
                cnt=1+heapq.heappop(max_heap) ## this is where a sequence if executed
                if cnt:
                    queue.append([cnt,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap,queue.popleft()[0])

        return time                