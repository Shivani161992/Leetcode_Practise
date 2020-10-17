s = "AB"
numRows = 1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        zigzag= [[] for i in range(0, numRows)]
        top=0
        bottom = len(zigzag)
        counter=0
        incre= True
        for i in range(0, len(s)):
            if counter== top:
                zigzag[counter].append(s[i])
                counter= counter +1
                incre= True
            elif counter== bottom -1:
                zigzag[counter].append(s[i])
                counter= counter -1
                incre= False
            else:
                if incre== True:
                    zigzag[counter].append(s[i])
                    counter = counter + 1
                elif incre== False:
                    zigzag[counter].append(s[i])
                    counter = counter - 1

        conver= [ele for sub in zigzag for ele in sub]
        return ''.join(conver)


obj= Solution()
print(obj.convert(s, numRows))