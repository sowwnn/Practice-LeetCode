# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head
        
        oddptr = current = head 
        evenptr = evenhead = head.next 
        i = 1
        
        while current:
            if i > 2: 
                if i % 2:  oddptr.next = oddptr  = current
                else:     evenptr.next = evenptr = current
            current = current.next 
            i += 1
            
        evenptr.next, oddptr.next = None, evenhead
        
        return head
    
    
