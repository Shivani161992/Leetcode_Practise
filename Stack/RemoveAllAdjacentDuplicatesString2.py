s = "abcd"
k= 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack_str=[]
        stack_count=[]
        for i in s:
            lstack=len(stack_str)
            if lstack==0:
                stack_str.append(i)
                stack_count.append(1)
            else:
                get_element = stack_str[lstack-1]
                if i == get_element:
                    get_count = stack_count[len(stack_count)-1]
                    if k == get_count+1:
                        stack_str.pop()
                        stack_count.pop()
                    elif k != get_count + 1:
                        stack_count[len(stack_count)-1]= get_count + 1

                else:
                    stack_str.append(i)
                    stack_count.append(1)
        return ''.join([stack_str[i] * stack_count[i] for i in range(0, len(stack_str))])


o=Solution()
y= o.removeDuplicates(s, k)
print(y)