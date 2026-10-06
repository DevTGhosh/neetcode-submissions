# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        prev = head
        newList = ListNode()
        prevNewList = newList
        arrayOld = []
        while curr:
            arrayOld.append(curr.val)
            curr = curr.next
        arrayOld.reverse()
        for index, value in enumerate(arrayOld):
            newList.val = value
        index = 1
        head2 = ListNode(arrayOld[0])
        curr2 = head2
        while index != len(arrayOld):
            newNode = ListNode(arrayOld[index])
            curr2.next = newNode
            curr2 = curr2.next
            index += 1
        return head2

