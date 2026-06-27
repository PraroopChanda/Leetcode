class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited=set()
        min_heap=[]
        heapq.heappush(min_heap,[nums1[0]+nums2[0],0,0])
        visited.add((0,0)) 
        output=[]

        while min_heap and k:
            sum1,r,c=heapq.heappop(min_heap)
            output.append([nums1[r],nums2[c]])
            k-=1

            if r+1<len(nums1) and (r+1,c) not in visited:
                heapq.heappush(min_heap,[nums1[r+1]+nums2[c],r+1,c])
                visited.add((r+1,c))

            if c+1<len(nums2) and (r,c+1) not in visited:
                heapq.heappush(min_heap,[nums1[r]+nums2[c+1],r,c+1])
                visited.add((r,c+1))

        return output            


            ## now add the next 2 smallest elements with their sum as a key into the heap
            

        
        