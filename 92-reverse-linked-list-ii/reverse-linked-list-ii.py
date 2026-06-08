# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        # Step 1: move prev to the node before `left`
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # prev is now before the part we want to reverse
        curr = prev.next

        # Step 2: reverse by moving nodes after curr to the front
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next