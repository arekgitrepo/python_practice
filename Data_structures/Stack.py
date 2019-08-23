class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class StackImpl(object):
    def __init__(self):
        self.count = 0
        self.top = None

    def push(self,data):
        self.count+=1
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        self.count -= 1
        if self.top:
            data = self.top.data
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def iter(self):
        current = self.top
        while current:
            yield current.data
            current=current.next

st = StackImpl()
st.push(1)
#st.push(2)
#st.push(3)
#st.push(4)

print(st.top)
st.pop()
st.pop()
print(st.top)

for ele in st.iter():
    print(ele,end=" ")













