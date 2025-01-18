class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head =  None
    
    def insertAtBegining(self,data):
        node = Node(data,self.head)
        self.head = node 

    def insertAtEnd(self,data):
        temp = self.head
        prev = None
        while temp:
            prev=temp
            temp=temp.next 
        prev.next = Node(data,None)
        
    def insertAtPosition(self, data, pos):
        temp = self.head
        prev=None
        
        while temp and pos>0:
            prev=temp
            temp=temp.next 
            pos-=1
        prev.next = Node(data,temp)
    
    def displayLinkedList(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        curr = self.head 
        while curr:
            print(curr.data,end="-->")
            curr=curr.next 
        print()
    


linkedList = LinkedList()
linkedList.insertAtBegining(1)
linkedList.insertAtBegining(2)
linkedList.insertAtBegining(3)
linkedList.displayLinkedList()
linkedList.insertAtEnd(10)
linkedList.displayLinkedList()
linkedList.insertAtPosition(11,2)
linkedList.displayLinkedList()
        