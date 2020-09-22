class MaxStack:

    def __init__(self):
        self.max_stack = []


    def push(self, x: int) -> None:
        self.max_stack.append(x)


    def pop(self) -> int:
        if len(self.max_stack) != 0:
            pop= self.max_stack.pop()

            return pop

    def top(self) -> int:
        if len(self.max_stack) != 0:
            return self.max_stack[-1]
        

    def peekMax(self) -> int:
        if len(self.max_stack) != 0:
            return max(self.max_stack)
        

    def popMax(self) -> int:
        if len(self.max_stack) != 0:
            max_ele=self.max_stack.pop()
            for i in range(len(self.max_stack)-1,-1, -1 ):
                if self.max_stack[i]==max_ele:
                    return self.max_stack.pop(i)

        

stack =  MaxStack()
stack.push(5); 
print(stack.peekMax())
print(stack.popMax())
