class Song:
    def __init__(self,name,genre,durations):
        self.name=name
        self.genre=genre
        self.durations=int(durations)
    def show_info(self):
        return f"{self.name} <|> {self.genre} <|> {self.durations//60}.{self.durations%60:>02}"
class DataNode:
    def __init__(self, data=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def enqueue(self, item: "Song"):
        pNew=DataNode(item)
        if not self.rear:
            self.front = self.rear = pNew
        else:
            self.rear.next = pNew
            self.rear = pNew
        self.count+=1
    def dequeue(self):
        if not self.front:
            print("Underflow! Dequeue from an empty queue")
            return None
        dequeue = self.front
        self.front=self.front.next
        if not self.front:
            self.rear = None
        self.count -= 1
        print(f"Dequeue item: {dequeue.data.show_info()}")
        return dequeue.data
    def peek(self):
        if not self.front:
            print("Underflow! Dequeue from an empty queue")
            return None
        return self.front.data
    def isEmpty(self):
        return self.front is None
    def show_Queue(self):
        if not self.front:
            print("Queue is empty!")
        else:
            current = self.front
            n=1
            while current:
                print(f"Queue#{n} {current.data.show_info()}")
                n+=1
                current = current.next
    def lastSong(self,time):
        if self.isEmpty():
            print("Nothing here! Please add some song")
        total_duration = 0
        current = self.front
        while current:
            total_duration += current.data.durations
            current = current.next
        time %= total_duration
        current = self.front
        n=1
        while current:
            if time < current.data.durations:
                print(f"Queue#{n} {current.data.show_info()}")
                return
            n+=1
            time -= current.data.durations
            current = current.next
    def removeSong(self,name):
        current = self.front
        previous = None
        found = False
        while current:
            if current.data.name == name:
                found = True
                if previous:
                    previous.next = current.next
                else:
                    self.front = current.next
                if current == self.rear:
                    self.rear = previous
                self.count -= 1
                print(f"Removed: {name}")
                return
            previous = current
            current = current.next
        if not found:
            print(f"Can not Delete! {name} is not exist")
    def groupSong(self):
        pass
    def undo(self):
        pass
    def rev_queue(self):
        pass
def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()