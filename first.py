import keyword

print(keyword.kwlist)

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

"""exponent of a number"""

exp = 2 ** 5
print(exp)

print("*********")

a = True

a = bool

print(bool(3))

print("*********")

a = "anu_deep"

print(a.replace("anu", "una", 1))

print(a.split(sep="_")[0])

city = "sfo"

print("welcome to %s" % city)

l = ["one", "two"]

print(l.count("one"))

dict = {"name": "anudeep", "age": 27}

print(dict.keys())

i = 8
if (i > 10):
    print("greater than 10")
elif (i == 10):
    print("equals 10")
else:
    print("none")

l = []
l.append(1)
print("length of list is %s" % len(l))
print(l.count(0))
print(type(l))
#for i in range(10):
#    print(i, end=" ")

print("*"*20)

def addition(n1, n2):
    return n1+n2

print(addition(10,20))

s="string"
s.upper()

class Car():
    def __init__(self,make,model="base"):
        self.make=make
        self.model=model

c1 = Car("Benz","CLA250")
print(c1.make)
print(c1.model)

c2 = Car("BMW")
print(c2.make)
print(c2.model)

from math import sqrt
print(sqrt(100))