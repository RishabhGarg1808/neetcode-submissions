# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        linked_list = ListNode(0)
        head = linked_list

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                linked_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                linked_list.next = ListNode(list2.val)
                list2 = list2.next
            
            linked_list = linked_list.next
        
        while list1 is not None:
            linked_list.next = ListNode(list1.val)
            linked_list = linked_list.next
            list1 = list1.next
        
        while list2 is not None:
            linked_list.next = ListNode(list2.val)
            linked_list = linked_list.next
            list2 = list2.next

        return head.next


        
        