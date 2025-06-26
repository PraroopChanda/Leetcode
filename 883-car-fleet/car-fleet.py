class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet=[]
        dict_1={key:value for key,value in zip(position,speed)}
        dict_1=dict(sorted(dict_1.items())) ## sorting with respect to keys- position
        for x in dict_1.keys():
            while car_fleet and (((target-x)/dict_1[x])>=car_fleet[-1]):
                car_fleet.pop()
            car_fleet.append((target-x)/dict_1[x]) 

        return len(car_fleet)         