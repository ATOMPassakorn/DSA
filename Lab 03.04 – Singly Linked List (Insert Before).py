class DataNode:
    def __init__(self, data=None):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.count=0
        self.head=None
    def insert_last(self,data):
        pNew=DataNode(data)
        if self.head is None:
          self.head = pNew
        else:
            start=self.head
            while start.next is not None:
                start=start.next
            start.next=pNew
        self.count+=1
    def insert_front(self,data):
       pNew=DataNode(data)
       pNew.next=self.head
       self.head=pNew
       self.count+=1
    def insert_before(self,node,data):
        if self.head is None:
            print("Cannot insert, "+node+" does not exist.")
            return
        pNew=DataNode(data)
        start=self.head
        prev=None
        while start is not None:
            if start.data==node:
                pNew.next=start
                if prev is None:
                    self.head=pNew
                else:
                    prev.next=pNew
                self.count+=1
                return
            prev=start
            start=start.next
        print("Cannot insert, "+node+" does not exist.")
    def traverse(self):
        start=self.head
        if start:
            while start is not None:
                if start.next is not None:
                    print(start.data, end=" -> ")
                else:
                    print(start.data, end="")
                start = start.next
        else:
            print("This is an empty list.")
def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #    mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()
main()