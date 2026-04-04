class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[-1]

    def size(self):
        return len(self.data)

class Queue:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, item):
        self.data.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Queue is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        raise IndexError("Queue is empty")
    
    def size(self):
        return len(self.data)

def reverse_string(text):
    new_string = ""
    source = Stack()
    for character in text:
        source.push(character)
    while not source.is_empty():
        new_string += source.pop()
    return new_string

def bank_simulation():
    bank_line = Queue()
    bank_line.enqueue("Harry")
    bank_line.enqueue("Jeff")
    bank_line.enqueue("Margaret")
    bank_line.enqueue("Catherine")
    bank_line.enqueue("Paul")
    while not bank_line.is_empty():
        customer = bank_line.dequeue()
        print(f"{customer} is now being served. {bank_line.size()} customers remaining")

bank_simulation()
