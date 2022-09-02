# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = ""
        while True:
            st += str(head.val)
            head = head.next
            if head == None:
                break
        if st == st[::-1]:
            return True
        else: return False
        
            
