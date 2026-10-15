# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        prev = None
        curr = head
        
        # Traverse the list and flip the pointers
        while curr:
            next_node = curr.next  # Save the remaining list
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        return prev