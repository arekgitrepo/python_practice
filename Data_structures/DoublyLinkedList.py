class Node(object):
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

class DoublyLinkedList(object):
    def __init__(self):
        self.count = 0
        self.head  = None #First element of the list
        self.tail = None #Last element of the list

    def append(self,val):
        new_node = Node(val,None,None)
        self.count+=1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self,val):
        current = self.head
        while current:
            if current.data == val:
                print("Element found in the list")
                return True
            current = current.next
        print("Element not found in the list")
        return False

    def delete(self,val):
        node_deleted = False
        current = self.head
        if self.search(val):
            if current is None:
                node_deleted = False
            elif current.data == val:
                self.head = current.next
                self.head.prev = None
                node_deleted = True
            elif self.tail.data == val:
                self.tail = self.tail.prev
                self.tail.next = None
                node_deleted = True
            else:
                while current:
                    if current.data == val:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                        node_deleted = True
                    current = current.next
        if node_deleted:
            self.count -= 1
            print("Element deleted from the list")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print(dll.tail)

for e in dll.iter():
    print(e)

print(dll.search(3))
dll.delete(2)
for e in dll.iter():
    print(e)
print("#"*10)
print(dll.head)
print(dll.tail)
