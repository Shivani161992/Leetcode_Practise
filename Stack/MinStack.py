class MinStack:

    def __init__(self):
        self.min_stack=[]
        self.min_element=[]

        
    def push(self, x: int) -> None:
        if len(self.min_stack) ==0:
            self.min_stack.append(x)
            self.min_element.append(x)
        else:
            prev= self.min_element[len(self.min_element)-1]
            self.min_stack.append(x)
            self.min_element.append(min(prev, x))

    def pop(self) -> None:
            if len(self.min_stack) !=0:
                self.min_stack.pop()
                self.min_element.pop()

    def top(self) -> int:
        if len(self.min_stack) !=0:
            return self.min_stack[len(self.min_stack)-1]
            
        

    def getMin(self) -> int:
        if len(self.min_stack) !=0:
            return self.min_element[len(self.min_element)-1]
        



m= MinStack();
m.push(-2);
m.push(0);
m.push(-3);
print(m.getMin()) # return -3
m.pop();
print(m.top())  # return 0
print(m.getMin()) # return -2