class TimeMap:

    def __init__(self):
        self.dict_1={}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict_1.keys():
            self.dict_1[key].append((value,timestamp))
        else:
            self.dict_1[key]=[(value,timestamp)] 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_1:
            return ""
        else:
            left=0
            right=len(self.dict_1[key])-1    
            if self.dict_1[key][left][1]>timestamp:
                return ""
            elif timestamp>self.dict_1[key][-1][1]:
                return self.dict_1[key][-1][0]    
            while right>=left:
                mid=(left+right)//2
                ts_value=self.dict_1[key][mid][1]
                if ts_value==timestamp:
                    return self.dict_1[key][mid][0]
                if ts_value>timestamp:
                    right=mid-1
                else:
                    left=mid+1      
            return self.dict_1[key][right][0] 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)