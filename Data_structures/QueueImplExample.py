from random import randint

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
            print("Queue is empty")
            return None

    def iter(self):

        current = self.tail
        while current:
            yield current.data
            current = current.next

class Track(object):
    def __init__(self,name):
        self.name = name
        self.length = randint(4,8)

# t1 = Track("hellooooo")
# t2 = Track("byeee")
# print(t1.length)
# print(t2.length)

import time
class Mediaplayer(QueueNode):
    def __init__(self):
        super().__init__()

    def add_track(self,track):
        self.enqueue(track)

    def play(self):
        while self.size>0:
            current_track = self.dequeue()
            print("Current playing track is {}".format(current_track.name))
            time.sleep(current_track.length)

t1 = Track("hellooooo")
t2 = Track("byeee")
t3 = Track("namasthe")
t4 = Track("tataaa")

mp = Mediaplayer()
mp.add_track(t1)
mp.add_track(t2)
mp.add_track(t3)
mp.add_track(t4)
mp.play()