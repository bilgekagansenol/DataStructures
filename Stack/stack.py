
from .node import Node

class Stack:
    def __init__(self ):
        self.top = Node("Top")
    
    def is_empty(self):
        if self.top.next is None :
            print("nothing in stack")
            return 0 
        else:
            print("stack is not empty")
            return 1
        
    def push(self , data):
        new_node = Node(data)
        if self.top.next == None:
            self.top.next = new_node
        else:
            new_node.next = self.top.next
            self.top.next = new_node

    def pop(self ):
        if self.top.next == None:
            print("stack is already empty")
        else:
            temp_data = self.top.next.data
            temp = self.top.next
            self.top.next = temp.next
            return temp_data
        
    def peek(self):
        if self.top.next == None:
            print("stack is empty ")
        else:
            data = self.top.next.data
            return data
        
    def print_stack(self):
        temp = self.top.next
        while temp is not None:
            print(temp.data + "-->")
            temp = temp.next
        if temp is None:
            print("empty stack")

    def size(self):
        temp = self.top.next
        i = 0
        while temp is not None:
            i += 1
            temp = temp.next
        return i
