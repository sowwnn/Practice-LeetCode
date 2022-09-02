# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        sentinel = ListNode(next = head)
        while head:
            arr.append(head.val)
            head = head.next
        
        arr.sort()
        temp = sentinel.next
        idx = 0
        while temp:
            temp.val = arr[idx]
            idx += 1
            temp = temp.next
        return sentinel.next
