# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: # find middle
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        slow.next = None
        prev = None
        while second: # reverse 2nd half
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        while second:
            firstTemp, secondTemp = first.next, second.next
            first.next = second
            second.next = firstTemp
            first = firstTemp
            second = secondTemp

