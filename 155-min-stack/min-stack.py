class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[] ## will be using this to track minimum
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack: 
            self.minstack.append(val)
        else: 
            self.minstack.append(min(self.minstack[-1],self.stack[-1]))

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()