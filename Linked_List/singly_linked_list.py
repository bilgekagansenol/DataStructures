from node import Node

class SinglyLinkedList:

    def __init__(self ,head : Node):
        self.head = head


    def is_empty(self):
        if not self.head.next :
            print("SinglyLinkedList is empty")
            return 1
        else:
            print("SinglyLinkedList is not empty")
            return 0          
    

    def append(self , new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
      
        if temp.next is None:
            temp.next = new_node
        else :
            print("there is an error about appending in Linked List")
    
    
    
    def prepend(self , new_data):
        new_node = Node(new_data)
        temp = self.head
        
        if temp.next is None:
            temp.next = new_node
            print("first node added")
        else:
            temp2 = temp.next
            temp.next = new_node
            new_node.next  = temp2
            print("new node prepended")
    


    def insert_after(self , new_data , index):
        ###    To Do
        pass