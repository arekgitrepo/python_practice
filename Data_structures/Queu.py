class QueueImplList(object):
    def __init__(self):
        self.count = 0
        self.items = []

    def enqueue(self,data):
        self.count+=1
        self.items.insert(0,data)

    def dequeue(self):
        self.count-=1
        data=self.items.pop()
        return data

ql = QueueImplList()
ql.enqueue(1)
ql.enqueue(2)
ql.enqueue(3)

for ele in ql.items:
    print(ele,end=" ")
ql.dequeue()
print()
for ele in ql.items:
    print(ele,end=" ")


# ql.items[0] = 5
# for ele in ql.items:
#     print(ele)

class Node(object):
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class QueueNode(object):
    def __init__(self):
        self.size = 0
        self.head = None #head is latest element
        self.tail = None #Tail is oldest element

    def enqueue(self,data):
        self.size+=1
        new_node = Node(data)
        if self.head:
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        current = self.tail
        if self.size == 1:
            self.size -= 1
            data = current.data
            self.head = None
            self.tail = None
            return data
        elif self.size > 1:
            self.size -= 1
            data = self.tail.data
            self.tail.next.prev = None
            self.tail = self.tail.next
            return data
        else:
            print("Queuee is empty")
            return None

    def iter(self):

        current = self.tail
        while current:
            yield current.data
            current = current.next

print()
print("*"*30)

qn = QueueNode()
qn.enqueue(1)
qn.enqueue(2)
qn.enqueue(3)
qn.enqueue(4)
print(qn.head)
print(qn.tail)
print(qn.dequeue())
print(qn.dequeue())

for ele in qn.iter():
    print(ele,end=" ")
print()
print(qn.head)
qn.dequeue()
qn.dequeue()
qn.dequeue()
