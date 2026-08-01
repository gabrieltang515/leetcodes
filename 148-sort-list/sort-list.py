class Solution:
    def sortList(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Base case:
        # A list with 0 or 1 node is already sorted.
        if head is None or head.next is None:
            return head

        # Step 1: Find the end of the first half.
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the linked list into two halves.
        second_half = slow.next
        slow.next = None

        # Step 3: Recursively sort both halves.
        left = self.sortList(head)
        right = self.sortList(second_half)

        # Step 4: Merge the two sorted halves.
        return self.merge(left, right)

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        # Compare one node from each list.
        while left is not None and right is not None:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # One list may still contain nodes.
        if left is not None:
            current.next = left
        else:
            current.next = right

        return dummy.next