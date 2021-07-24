from typing import List
import abc
from abc import ABC, abstractmethod
postfix = ["3", "4", "+", "2", "*", "7", "/"]

class Treenode(Node):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.operations={'+': self.addition, '-': self.subtration, '*': self.multiplication, '/': self.division}

    def evaluate(self) -> int:
        if self.val not in self.operations:
            return int(self.val)
        else:
            return self.operations[self.val](self.left.evaluate(), self.right.evaluate())

    def addition(self, x, y):
        return x+y
    def subtration(self, x, y):
        return x-y
    def multiplication(self, x, y):
        return x*y
    def division(self, x, y):
        return x//y


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        root = None
        operations = ['+', '-', '*', '/']
        stack = []
        for p in postfix:
            if p not in operations:
                stack.append(p)
            elif p in operations:
                getNum2 = stack.pop()  # 4
                getNum1 = stack.pop()  # 3
                nodeOperation = Treenode(p)
                if type(getNum2) == str:
                    num2Node = Treenode(getNum2)
                else:
                    num2Node= getNum2

                if type(getNum1) == str:
                    num1Node = Treenode(getNum1)
                else:
                    num1Node = getNum1

                nodeOperation.left = num1Node
                nodeOperation.right = num2Node
                root= nodeOperation
                stack.append(nodeOperation)

        return root


obj = TreeBuilder()
print(obj.buildTree(postfix))
