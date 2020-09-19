homepage="jrbilt.com"
class BrowserHistory:
    def __init__(self, homepage: str):
        self.browser=[homepage]
        self.curr=0

    def visit(self, url: str) -> None:
        while len(self.browser)-1 > self.curr:
            self.browser.pop()
        self.browser.append(url)
        self.curr= len(self.browser)-1

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr= 0
            return self.browser[0]
        elif steps <= self.curr:
            self.curr= self.curr - steps
            return self.browser[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr+steps < len(self.browser):
            self.curr= self.curr + steps
            return self.browser[self.curr]
        elif self.curr+steps >= len(self.browser):
            self.curr= len(self.browser)-1
            return self.browser[self.curr]

obj=BrowserHistory(homepage)
obj.visit("uiza.com")
print(obj.forward(3))
print(obj.forward(3))
obj.visit("fveyl.com")
obj.visit("hyhqfqf.com")
print(obj.back(3))
obj.visit("cccs.com")
obj.visit("bivz.com")
print(obj.forward(6))
print(obj.back(1))
obj.visit("cmbw.com")
obj.visit("iywwwfn.com")
obj.visit("sktbhdx.com")
print(obj.forward(8))
print(obj.forward(10))
obj.visit("bskj.com")
obj.visit("thw.com")
print(obj.back(6))
obj.visit("hgesj.com")
print(obj.forward(6))
obj.visit("ctb.com")
obj.visit("fllnc.com")
obj.visit("fs.com")
print(obj.back(7))
