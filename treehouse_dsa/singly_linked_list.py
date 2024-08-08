class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes = data and the link to the next node in the list
    """
    data = None
    nextNodeAddress = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class SinglyLinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None
# Adding methods to make the use of data structure easier

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list. Takes O(n) time (Linear time)
        """
        current = self.head
        count = 0  # local variable

        while current != None:
            count += 1
            current = current.nextNodeAddress
        return count

    def add(self, data):
        """
        Adds new node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.nextNodeAddress = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches for the first node containing data according to the key
        It returns the node if found and 'None' is node is not found
        Takes O(n) time

        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.nextNodeAddress
        return None

    def __repr__(self):
        """
        Returns a string represenation of a list
        Takes O(n) time
        """
        nodes = []  # start by creating an empty list
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.nextNodeAddress is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.nextNodeAddress
        return '->'.join(nodes)


# TODO: Insert and Delete in Linked list (2:48 Hrs Contd.)
