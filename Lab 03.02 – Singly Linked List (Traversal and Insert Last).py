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
    mylist.insert_last(input())
  mylist.traverse()
main()