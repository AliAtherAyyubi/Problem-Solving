# Add two numbers 

class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

# Insert into end
    def insert(self,data):
        new_node = Node(data)

        if self.head==None:
            self.head=new_node
            return
        
        last= self.head
        while (last.next):
            last=last.next

        last.next= new_node

    # add two numbers
def addTwoNumbers(l1, l2):
    number=0
    while l1.head!=None:
        number = number*10 + l1.head.data
        l1.head=l1.head.next
    number2=0
    while l2.head!=None:
        number2 = number2*10 + l2.head.data
        l2.head=l2.head.next

    sum= int(number)+int(number2)

    sum= str(sum)[::-1]

    newList= LinkedList()

    for digit in sum:
        # print(type(digit))
        newList.insert(int(digit))
    
    return newList


if __name__ == '__main__':

    list1 = LinkedList()
    list2 = LinkedList()

    l1 = [2,4,9]

    l2 = [5,6,4,9]

    for x in l1:
        list1.insert(x)
        
    for  y in l2:
        list2.insert(y)

    list1= addTwoNumbers(list1,list2)

    # print(list1.head.data)
    while list1.head!=None:
        print(list1.head.data)
        list1.head=list1.head.next
        



    
   

# digits=[2,4,3]
# number=0
# for digit in digits:
#     number=number*10+ digit

# number=int(str(number)[::-1])
# print(type(number))