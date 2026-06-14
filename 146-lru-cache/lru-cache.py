class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """
        Remove node from its current position.
        """
        prev_node = node.prev
        next_node = node.next

        # Linking the previous node and the next node together
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_recent(self, node):
        """
        Add node right before tail.
        This makes it the most recently used node.
        """
        prev_node = self.tail.prev

        # Setting relationship between previous "front" most node and new frontmost node
        prev_node.next = node
        node.prev = prev_node

        # Setting relationship between tail and new frontmost node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Since we used this key, move it to most recent
        self.remove(node)
        self.add_to_recent(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            old_node = self.cache[key]

            # Remove old position
            self.remove(old_node)

            # Update value
            old_node.value = value

            # Move to most recent
            self.add_to_recent(old_node)

        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_recent(new_node)

            if len(self.cache) > self.capacity:
                # Remove least recently used node
                lru_node = self.head.next

                self.remove(lru_node)
                del self.cache[lru_node.key] #del can remove from the hashmap