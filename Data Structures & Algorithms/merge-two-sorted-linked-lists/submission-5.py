# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        currVal = -101
        if list1 and list2 and list1.val <= list2.val:
            currVal = list1.val
            list1 = list1.next
        elif list1 and list2 and list2.val < list1.val:
            currVal = list2.val
            list2 = list2.next
        elif list1 and not list2:
            currVal = list1.val
            list1 = list1.next
        elif list2 and not list1:
            currVal = list2.val
            list2 = list2.next
        else:
            return
        curr = ListNode(currVal)
        head = curr
        while list1 or list2:
            nextVal = curr.val
            if list1 and list2:
                nextVal = min(list1.val, list2.val)
            elif list1 and not list2:
                nextVal = list1.val
            elif list2 and not list1:
                nextVal = list2.val
            else:
                break
            if list1 and list1.val == nextVal:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            elif list2 and list2.val == nextVal:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
            else:
                break
        return head
