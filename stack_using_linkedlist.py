class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Stack_implementation:
      def __init__(self):
            self.head=None
      def  display(self):
            temp=self.head
            while(temp!=None):
                  print(temp.data)
                  temp=temp.next
           
      def  push(self,data):
            temp=Node(data)
            temp1=self.head
            if  self.head==None:
                  self.head=temp
            else:
                  while(temp1.next!=None):
                        temp1=temp1.next
                  temp1.next=temp
      def pop(self):
            temp=self.head
            temp1=temp.next
            while(temp1.next!=None):
                  temp1=temp1.next
                  temp.next=temp1
            temp.next=None
            self.display()
obj=Stack_implementation()
ch=0
while(ch!=4):
      print('1.push','2.pop','3.display','4.exit')
      ch=int(input())
      if ch==1:
            print("enter the data to be added to the stack")
            data=int(input())
            obj.push(data)
            obj.display()
      if ch==2:
            obj.pop()
            obj.display()
      if ch==3:
            obj.display()
            
