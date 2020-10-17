from typing import List
trabnsactions= ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for one_trans in range(0, len(transactions)):
            hold = transactions[one_trans].split(sep=",")
            name = hold[0]
            time = hold[1]
            amount = hold[2]
            city = hold[3]
            if int(amount) > 1000:
                one_trans = ','.join(hold)
                invalid.append(hold)

            for trans in range(one_trans + 1, len(transactions)):
                trans = transactions[trans].split(sep=",")
                name2 = trans[0]
                time2 = trans[1]
                amount2 = int(trans[2])
                city2 = trans[3]

                if name == name2 and abs(int(time) - int(time2)) <= 60 and city != city2:
                    one_trans = ','.join(one_trans)
                    trans = ','.join(trans)
                    invalid.append(one_trans)
                    invalid.append(trans)
        return list(set(invalid))


obj=Solution()
obj.invalidTransactions(trabnsactions)
