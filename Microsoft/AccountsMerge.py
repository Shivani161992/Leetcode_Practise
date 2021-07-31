from  typing import List
from collections import defaultdict
accounts = [["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if len(accounts) >1:
            adjList=defaultdict(list)
            for account in accounts:
                name= account[0]
                emails= set(account[1:])
                if name not in adjList:
                    adjList[name].append(emails)
                elif name in adjList:
                    getAccounts=adjList[name]
                    found=0
                    for j in range(0, len(getAccounts)):
                        for i in range(1, len(account)):
                            x= account[i]
                            if account[i] in getAccounts[j]:
                                found=1
                                for k in range(1, len(account)):
                                    getAccounts[j].add(account[k])
                                break
                        if found==1:
                            break
                    if found==0:
                        adjList[name].append(emails)

            output=[]
            for person in adjList:
                accs= adjList[person]
                for ac in accs:
                    combined=[person]
                    for h in ac:
                        combined.append(h)
                    combined.sort()
                    output.append(combined.copy())
            return output





obj=Solution()
print(obj.accountsMerge(accounts))
