###STACK IMPLEMENTATION###
def push1(list1,element):
      list1.insert(0,element)
      return list1
def pop():
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
                  print('|',i,'|')
                  print('  __')
ch=0
list1=[]
while(ch!=4):
      print('1.push','2.pop','3.display','4.exit')
      ch=int(input())
      if ch==1:
            element=int(input("enter the element to be pushed"))
            d=push1(list1,element)
            display(list1)
      if ch==2:
            pop()
            display(list1)
      if ch==3:
            display(list1)
            
             
                  

