class ListNode:
    def __init__(self, val=".", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.tail = self.head
        self.currentPage = self.head

    def visit(self, url: str) -> None:
        self.currentPage = ListNode(url, self.currentPage)
        prevPage = self.currentPage.prev
        self.tail = self.currentPage
        prevPage.next = self.currentPage
        print("visit url:",url)
        return None

    def back(self, steps: int) -> str:
        if self.currentPage == self.head:
            return self.head.val
        print("back steps:", steps)
        while steps > 0 and self.currentPage != self.head:
            if self.currentPage.prev is None:
                print("prev issue val",self.currentPage.val)

            self.currentPage = self.currentPage.prev
            steps -= 1
        return self.currentPage.val

    def forward(self, steps: int) -> str:
        if self.currentPage == self.tail:
            return self.tail.val
        print("fwd steps:", steps)
        while steps > 0 and self.currentPage != self.tail:
            self.currentPage = self.currentPage.next
            steps -=1
        return self.currentPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
