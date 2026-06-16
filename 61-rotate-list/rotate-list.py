# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None


        length = 1
        end_ptr = head
        while end_ptr.next != None:
            end_ptr = end_ptr.next
            length += 1

        # Connecting to form a circle
        end_ptr.next = head

        # Find new tail and detach
        k = k % length
        to_move = length - k - 1

        for i in range(to_move):
            head = head.next

        new_head = head.next
        head.next = None

        return new_head



        