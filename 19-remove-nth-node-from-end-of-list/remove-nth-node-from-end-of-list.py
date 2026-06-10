class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches None
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now right before the node to remove
        slow.next = slow.next.next

        return dummy.next