class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ## removing triplets that cannot be considered
        list_1=[]
        x=target[0]
        y=target[1]
        z=target[2]
        x_bool=False
        y_bool=False
        z_bool=False
        for trip in triplets:
            if trip[0]>x or trip[1]>y or trip[2]>z:
                pass
            else:
                list_1.append(trip)
                if not x_bool and trip[0]==x:
                    x_bool=True
                if not y_bool and trip[1]==y:
                    y_bool=True
                if not z_bool and trip[2]==z:
                    z_bool=True        
        if len(list_1)==0:
            return False

        if x_bool and y_bool and z_bool:
            return True
        else:
            return False    
