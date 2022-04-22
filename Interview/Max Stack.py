class MaxStack:

    def __init__(self):

        self.stack = []
        self.maxStack = []
        

    def push(self, x: int) -> None:
        

        self.stack.append(x)
        if x>= self.maxStack[-1] or self.maxStack:
            self.maxStack.append(x)

    def pop(self) -> int:
        
       
        if self.stack[-1] == self.maxStack[-1]:
            self.maxStack.pop()

        return self.stack.pop()

        

    def top(self) -> int:

        return self.stack[-1]
        

    def peekMax(self) -> int:
        
        if self.maxStack:
            return self.maxStack[-1]
        

    def popMax(self) -> int:


        temp = []

        while self.stack[-1] != self.maxStack[-1]:
            temp.append(self.stack[-1])
            self.stack.pop()

        res = self.stack.pop()
        self.maxStack.pop()

        while temp:

            self.push(temp[-1])
            temp.pop()

        return res




        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()