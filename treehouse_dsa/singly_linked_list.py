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

    # Add a new function
