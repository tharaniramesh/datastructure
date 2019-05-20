class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Queue_implementation:
      def __init__(self):
            self.head=None
      def  display(self):
            temp=self.head
            while(temp!=None):
                  print(temp.data)
                  temp=temp.next
           
      def  enqueue(self,data):
            temp=Node(data)
            temp.next=self.head
            self.head=temp
      def dequeue(self):
            temp=self.head
            temp1=temp.next
            while(temp1.next!=None):
                  temp1=temp1.next
                  temp.next=temp1
            temp.next=None
            
obj=Queue_implementation()
ch=0
while(ch!=4):
      print('1.enqueue','2.dequeue','3.display','4.exit')
      ch=int(input())
      if ch==1:
            print("enter the data to be added to the stack")
            data=int(input())
            obj.enqueue(data)
            obj.display()
      if ch==2:
            obj.dequeue()
            obj.display()
      if ch==3:
            obj.display()
            
