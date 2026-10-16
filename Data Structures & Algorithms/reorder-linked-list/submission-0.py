# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next  and fast.next.next:
            slow = slow.next
            fast=fast.next.next
        
        prev = None
        curr = slow.next
        slow.next =  None

        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start = head
        while prev and  start:
            temp1 =start.next
            temp2 = prev.next

            start.next = prev
            prev.next = temp1

            start = temp1
            prev = temp2
        


        

