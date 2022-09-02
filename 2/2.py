class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNumber(l):
            vt, num = 0, 0
            while l:
                num += l.val * 10 ** vt
                vt += 1
                l = l.next
            return num
        n = getNumber(l1)+ getNumber(l2)
        head = ListNode()
        curr, prev = head, head
        for s in reversed(str(n)):
            curr.val = int(s)
            curr.next = ListNode()
            prev = curr
            curr = curr.next
        prev.next = None
        return head
