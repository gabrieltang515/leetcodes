class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        # 1. Insert copied nodes after each original node
        ptr = head
        while ptr:
            copy = Node(ptr.val)
            copy.next = ptr.next
            ptr.next = copy
            ptr = copy.next

        # 2. Assign random pointers for copied nodes
        ptr = head
        while ptr:
            copy = ptr.next

            if ptr.random:
                copy.random = ptr.random.next
            else:
                copy.random = None

            ptr = copy.next

        # 3. Separate the copied list from the original list
        ptr = head
        deep_head = head.next

        while ptr:
            copy = ptr.next
            next_original = copy.next

            ptr.next = next_original

            if next_original:
                copy.next = next_original.next
            else:
                copy.next = None

            ptr = next_original

        return deep_head