class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_length=len(nums)
        if num_length==1:
            return [-1]    
        output=[-1 for _ in range(len(queries))]
        dict_1={}
        for x in range(num_length):
            if nums[x] in dict_1:
                dict_1[nums[x]].append(x)  
            else:
                dict_1[nums[x]]=[x]
        answer=[-1] * num_length ## basically mapping all distances for each num
        for val,indices in dict_1.items():
            list_len=len(indices)
            if list_len==1:
                continue
            for i in range(list_len):
                curr=indices[i]
                prev=indices[(i-1)%list_len] ## because of cycle
                next_idx=indices[(i+1)%list_len]
                prev_dist=min(abs(curr-prev),num_length-abs(curr-prev))
                next_dist=min(abs(curr-next_idx),num_length-abs(curr-next_idx))

                answer[curr]=min(prev_dist,next_dist)
        return [answer[q] for q in queries]      

                    


        # for index in range(len(queries)):
        #     query=queries[index]
        #     if len(dict_1[nums[query]])==1 :
        #         continue
        #     min_dist=num_length    
        #     for val in dict_1[nums[query]]:
        #         dist = min(abs(query - val), num_length - abs(query - val))
        #         if val!=query and dist<min_dist:
        #             min_dist=dist

        #     output[index]=min_dist

        # return output            



        