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
        
        new_node = Node(new_data)
        temp = self.head
        
        for i in range(0,index ):
            if temp == None:
                print("list is not longer than index that user given")
                raise IndexError("invalid index")
            temp = temp.next
        if temp.next == None:
            temp.next = new_node
            print("added on last index that you selected")
        else:
            new_node.next = temp.next
            temp.next = new_node
            print("inserted after given index")
         
    
    def delete(self , data):
        temp = self.head
        while not temp.next.data == data or temp.next== None :
            temp = temp.next
          ## need to fix 
        if temp==None:
            print("cannot found data that match in list")
        else:
            if temp.next.next == None:
                temp.next = None
            else:
                temp2 = temp.next
                temp.next = temp2.next
                temp2 = None

                
            

