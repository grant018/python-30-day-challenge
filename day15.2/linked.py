class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
      self.head = None

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, value):
        current = self.head
        previous = None

        # Case 1: deleting the head
        if current is not None and current.value == value:
            self.head = current.next
            return

        # Case 2: deleting somewhere in the middle or end
        while current is not None:
            if current.value == value:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False