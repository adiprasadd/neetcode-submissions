# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listInit = ListNode(0)
        listinittemp = listInit
        carry = 0
        while l1 or l2:
            if not l1.next and l2.next:
                l1.next = ListNode(0)
            elif l1.next and not l2.next:
                l2.next = ListNode(0)
            temp = l1.val + l2.val + carry
            carry = 0
            if temp > 9:
                carry = 1
                temp = temp-10
            listinittemp.next = ListNode(temp)
            listinittemp = listinittemp.next
            l1 = l1.next
            l2 = l2.next
        if carry == 1:
            listinittemp.next = ListNode(1)

        return listInit.next