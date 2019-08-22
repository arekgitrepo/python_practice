from Data_structures.SinglyLinkedLisy import Node

class SinglyCircularLinkedListEnhanced:
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
            self.head.next = self.tail #Circular List change

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
            while prev != self.head or prev == current: #Circular List change
                if current.data == val:
                    if current == self.tail:
                        self.tail = current.next
                        self.head.next = self.tail #Circlar List change
                    else:
                        prev.next = current.next
                    self.count -= 1
                    print("Deleted value")
                    return
                prev = current
                current = current.next
        else:
            print("Value is not present in the List to delete")


sle = SinglyCircularLinkedListEnhanced()
sle.append(5)
sle.append(6)
sle.append(7)
sle.append(8)

counter = 0
#Looping through circular List
for val in sle.iter():
    print(val)
    counter += 1
    if counter>100:
        break

