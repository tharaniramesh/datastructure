###QUEUE IMPLEMENTATION###
def enqueue(list1,element):
      list1.append(element)
      return list1
def dequeue():
       if len(list1)==0:
             print("invalid")
       else:
             del(list1[0])
       return list1      
def display(element):
      if (len(list1)==0):
                  print("empty list")
      else:
            for i in list1:
                  print("|",end="")
                  print("_",i,"_",end='')
                  print('|',end=" ")
ch=0
list1=[]
while(ch!=4):
      print('1.enqueue','2.dequeue','3.display','4.exit')
      ch=int(input())
      if ch==1:
            element=int(input("enter the element to be queued"))
            d=enqueue(list1,element)
            display(list1)
      if ch==2:
            dequeue()
            display(list1)
      if ch==3:
            display(list1)
            
