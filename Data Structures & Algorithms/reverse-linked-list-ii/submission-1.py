
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        i = 0
        curr = dummy

        # Move curr to the node just before left
        while i < left - 1:
            i += 1
            curr = curr.next

        ptr = curr
        prev = None
        curr = curr.next

        # Reverse links from left to right
        while i < right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        # Reconnect the reversed section
        ptr.next.next = curr
        ptr.next = prev

        return dummy.next
