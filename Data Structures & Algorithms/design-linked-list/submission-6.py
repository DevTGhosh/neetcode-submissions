class ListNode:
    def __init__(self, val=1001, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        currNode = self.head
        currIndex = 0
        while currIndex < index and currNode:
            currNode = currNode.next
            currIndex += 1

        if currNode:
            return currNode.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:

        if self.size == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            currNode = ListNode(val, self.head)
            self.head.prev = currNode
            self.head = currNode
        self.size += 1
        return None

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val, None, self.tail)
            self.tail = self.tail.next
        self.size += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        if index == 0:
            self.addAtHead(val)
            return None
        if index == self.size:
            self.addAtTail(val)
            return None
        currNode = self.head
        currIndex = 0

        while currIndex < index and currNode:
            currNode = currNode.next
            currIndex += 1

        newNode = ListNode(val, currNode, currNode.prev)
        currNode.prev.next = newNode
        currNode.prev = newNode

        self.size += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        currNode = self.head
        currIndex = 0
        while currIndex < index and currNode:
            currNode = currNode.next
            currIndex += 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == currNode:
            self.head = currNode.next
            self.head.prev = None
        elif self.tail == currNode:
            self.tail = currNode.prev
            self.tail.next = None
        else:
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev
        
        self.size -= 1 


