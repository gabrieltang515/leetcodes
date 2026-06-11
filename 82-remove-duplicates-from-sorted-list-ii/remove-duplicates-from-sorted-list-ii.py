# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        ptr1 = dummy
        ptr2 = head

        while ptr2:
            # If duplicate
            if ptr2.next and ptr2.val == ptr2.next.val:
                duplicate_value = ptr2.val

                while ptr2 and ptr2.val == duplicate_value:
                    ptr2 = ptr2.next

                ptr1.next = ptr2

            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

        return dummy.next        