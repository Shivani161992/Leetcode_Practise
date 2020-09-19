from typing import List

transactions = ["xnova,261,1949,chicago", "bob,206,1284,chicago", "xnova,420,996,bangkok", "chalicefy,704,1269,chicago",
                "iris,124,329,bangkok", "xnova,791,700,amsterdam", "chalicefy,572,697,budapest",
                "chalicefy,231,310,chicago", "chalicefy,763,857,chicago", "maybe,837,198,amsterdam",
                "lee,99,940,bangkok", "bob,132,1219,barcelona", "lee,69,857,barcelona", "lee,607,275,budapest",
                "chalicefy,709,1171,amsterdam"]


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [list(i.split(sep=',')) for i in transactions]
        trans.sort(key=lambda x: (x[0], int(x[1])))
        invalid = []
        for t in trans:
            if int(t[2]) > 1000:
                invalid.append(t)
            elif int(t[2]) <= 1000:
                for i in range(0, len(trans)):
                    if i != trans.index(t):  # names are equal
                        if trans[i][0] == t[0] and trans[i][3] != t[3] and abs(int(trans[i][1]) - int(t[1])) <= 60:
                            invalid.append(t)
                    elif trans[i][0] != t[0]:
                        break
        inv = [','.join(i) for i in invalid]
        return inv


obj = Solution()
print(obj.invalidTransactions(transactions))
