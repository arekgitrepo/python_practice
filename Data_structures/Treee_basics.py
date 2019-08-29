class Node(object):

    def __init__(self,data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

from collections import deque

class BinTreee(object):

    def __init__(self):
        self.num_element = 0
        self.root_node = None

    def insert(self,data):
        self.num_element += 1
        new_node = Node(data)
        if self.root_node is None:
            self.root_node = new_node
        else:
            parent = self.root_node
            while True:
                if new_node.data < parent.data:
                    if parent.left_child is None:
                        parent.left_child = new_node
                        return
                    else:
                        parent = parent.left_child
                else:
                    if parent.right_child is None:
                        parent.right_child = new_node
                        return
                    else:
                        parent = parent.right_child

    def get_parent_node(self,data):
        parent = None
        node = Node(data)
        if self.root_node is None:
            return False
        else:
            if node.data == self.root_node:
                return parent,node
            else:
                current = self.root_node
                parent = None
                while True:
                    if current.data == node.data:
                        return parent, current
                    if node.data > current.data:
                        parent = current
                        current = current.right_child
                    else:
                        parent = current
                        current = current.left_child

    def remove(self,data):
        parent,node = self.get_parent_node(data)

        if parent is None and node is None:
            return False
        children = 0
        if node.left_child is None and node.right_child is None:
            children = 0
        elif node.left_child is not None and node.right_child is not None:
            children = 2
        else:
            children = 1

        if children == 0:
            if parent:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None
        elif children == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.right_child is node:
                    parent.right_child = next_node
                else:
                    parent.left_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self,data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data == data:
                return data
            elif data > current.data:
                current = current.right_child
            else:
                current = current.left_child

    ##Depth-First-Traversal
    #Inorder-Traversal(Left - Root - Right)
    #Preorder-Traversal(Root - Left - Right)
    #Postorder-Traversal(Left - Right - Root)
    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)

    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    #Breadth-First Traversal

    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node=traversal_queue.popleft()
            list_of_nodes.append(node)
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)

        return list_of_nodes


# n1 = Node(6)
# n2 = Node(5)
# n3 = Node(7)
# n4 = Node(4)
# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4

bst = BinTreee()
bst.insert(9)
bst.insert(10)
bst.insert(13)
bst.insert(1)
bst.insert(12)
bst.insert(7)
bst.insert(8)
bst.insert(5)

n1 = bst.root_node
while n1:
    print(n1.data)
    n1 = n1.left_child

parent,node = bst.get_parent_node(13)
print(parent.data,node.data)

for n in bst.breadth_first_traversal():
    print(n.data)