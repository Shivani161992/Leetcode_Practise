class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser=[homepage]
        self.ctr=0

    def visit(self, url: str) -> None:
        while self.ctr != len(self.browser)-1:
            self.browser.pop()
        self.browser.append(url)
        self.ctr=len(self.browser)-1

    def back(self, steps: int) -> str:
        if self.ctr - steps < 0:
            self.ctr= 0
            return self.browser[0]
        elif self.ctr - steps >= 0:
            self.ctr= self.ctr-steps
            return self.browser[self.ctr]


    def forward(self, steps: int) -> str:
        if steps + self.ctr > len(self.browser) - 1:
            self.ctr = len(self.browser) - 1
            return self.browser[self.ctr]
        elif steps + self.ctr <= len(self.browser) - 1:
            self.ctr = self.ctr + steps
            return self.browser[self.ctr]




browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");     #  // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");    # // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");     # // You are in "facebook.com". Visit "youtube.com"
print(browserHistory.back(1));                  # // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browserHistory.back(1));                   #// You are in "facebook.com", move back to "google.com" return "google.com"
print(browserHistory.forward(1));                #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     #// You are in "facebook.com". Visit "linkedin.com"
print(browserHistory.forward(2))                #// You are in "linkedin.com", you cannot move forward any steps.
print(browserHistory.back(2));                   #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browserHistory.back(7));                   #// You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

