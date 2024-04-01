from Node import Node

#Class of Doubly link list for efficiency
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #append function to add node in it
    def append(self, data):
        #Node class 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    #pop function to delete and remove link from the list
    def pop(self):
        if not self.tail:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data