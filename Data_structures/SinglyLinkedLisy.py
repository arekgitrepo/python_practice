class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


n = Node(10)
print(n)


class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.tail = None

    def append(self,data):
        n = Node(data)
        self.count += 1
        if self.tail is None:
            self.tail = n
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = n

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

sl = SinglyLinkedList()
sl.append(1)
sl.append(2)
sl.append(3)
sl.append(4)

for e in sl.iter():
    print(e)


class SinglyLinkedListEnhanced:
    def __init__(self):
        self.count = 0
        self.tail = None #First element of list
        self.head = None #Last element of List

    def append(self,data):
        n = Node(data)
        self.count += 1
        if self.head is None:
            self.tail = n
            self.head = n
        else:
            self.head.next = n
            self.head = n

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self,val):
        current = self.tail
        while current:
            if current.data == val:
                print("Value found in List")
                return True
            current = current.next
        print("Value is not found")
        return False

    def delete(self,val):
        if self.search(val):
            prev = self.tail
            current = self.tail
            while current:
                if current.data == val:
                    if current == self.tail:
                        self.tail = current.next
                    else:
                        prev.next = current.next
                    self.count -= 1
                    print("Deleted value")
                    return
                prev = current
                current = current.next
        else:
            print("Value is not present in the List to delete")
sle = SinglyLinkedListEnhanced()
sle.append(5)
sle.append(6)
sle.append(7)
sle.append(8)

print('#'*20)
for e in sle.iter():
    print(e)
sle.search(9)
print(sle.count)
sle.delete(8)
#print(sle.count)
for e in sle.iter():
    print(e)