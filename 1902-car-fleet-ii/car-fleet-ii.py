class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        output=[-1.0 for x in range(len(cars))]
        stack=[]
        for x in range(len(cars)-1,-1,-1):
            ## basically at this time the car is slower than the car ahead
            while (len(stack)!=0 and cars[x][1]<=cars[stack[-1]][1]):
                stack.pop()
            ## now this means that current car speed is greater than its forward one    
            while (len(stack)!=0):
                cl_time=float((cars[stack[-1]][0]-cars[x][0])/(cars[x][1]-cars[stack[-1]][1]))
                if cl_time<output[stack[-1]] or output[stack[-1]]==-1:
                    ## then this will collide first with the car in front and not any other car
                    output[x]=cl_time
                    break
                ## but in the case if front car collides with someone else, then i need to check with forward-forward cars
                stack.pop() 
            ## normal case when i just need to add elements or after i get a collison i still need to add elements    
            stack.append(x)
        return output    


        

        