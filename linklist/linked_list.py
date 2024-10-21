class Node:
    """
    An object for storing a single mode of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self , data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data # %s is replace value of self.data , e.g Node data : 10

class LinkedList:

    """ Singly linked list """
    def __init__(self):
            self.head = None

    def is_empty(self):
            return self.head == None

    def size(self):

            """Returns the number of nodes in the list
            Takes 0(n){linear} time"""

            current = self.head
            count = 0

            while current: #loop until current = 0
                count += 1
                current = current.next_node

            return count

    def add(self, data):
        """ Add new Node containing data at head of the list
        Takes 0(1) time"""
        new_node =Node(data)
        new_node.next_node = self.head
        self.head = new_node  # new node is adding at the start so new_node.next_node = self.head

    def search(self, key):
        """ Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """ Inserts a new Node containing data at index position
        Insertion take 0(1) time but finding the node at the
        insertion point takes 0(n) time."""
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -=1  # we take negative , we have to stop 1 index before
                # so that we connect prev node to new and new node to next_node

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """Remove Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Take 0(n) time"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head: # the  key is at head remove head
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index): #this function helps us to find the index fo the link-list
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):  #reper fxn used to represent string representation of an object
        """Return a string representation of the list
        Takes o(n) time"""

        nodes = []
        current = self.head

        while current:
            if current is self.head: # it cheak , is it a head then we print head: 10
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None: # it check if there is tail present or not , if not than its a tail
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data) # this is neither head nor tail

            current = current.next_node
        return '->' .join(nodes)
