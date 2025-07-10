from .node import Node

class SinglyLinkedList:

    def __init__(self ):
        self.head = Node("Head")


    def is_empty(self):
        if not self.head.next :
            print("SinglyLinkedList is empty")
            return 1
        else:
            print("SinglyLinkedList is not empty")
            return 0          
    
    def singl_printlist(self):
        temp = self.head.next
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    def singl_append(self , new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
      
        if temp.next is None:
            temp.next = new_node
        else :
            print("there is an error about appending in Linked List")
    
    
    
    def singl_prepend(self , new_data):
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
    


    def singl_insert_after(self , new_data , index):
        
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
         
    
    def singl_delete(self , data):
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

                
            
    def singl_delete_at(self , index):
        temp = self.head
        for i in range(index):
            if temp == None :
                break
            temp = temp.next
        temp.next = temp.next.next
        print("node is deleted")

    def singl_update(self , index , data):
        temp = self.head
        for i in range(index):
            if temp.next == None:
                break
            temp = temp.next
        if temp.next is None:
            print("out of index")
        temp.next.data = data
    