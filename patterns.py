i=1
while i<=4:
    print("#"*4)
    i+=1


print("Using for loop")

for i in range(4):
    for j in range(4):
        print("#",end='')

    print()

print("New pattern")

for i in range(1,5,1):
    j=1
    while j<=i:
        print("#",end='')
        j+=1
    print()

print("New pattern using nested for loop")

for i in range(4):
    for j in range(4-i):
        print("#",end='')
    print()

num=5
for i in range(2,num):
    if num%i == 0:
        print("Not Prime")
        break
else :
    print("Prime")

print(5//2)



print("Decorator example")

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        print(func.__name__)
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b

print((div(2,4)))


import array as arr

vals = arr.array('i',[1,3,-4,7,8])

print(vals)

print(vals.buffer_info()[1])

print(len(vals))

for i in range(vals.buffer_info()[1]):
    print(vals[i])

new_vals = arr.array(vals.typecode,(a for a in vals))

print("*"*10)

for i in new_vals:
    print(i,end=" ")

from array import *

arr = array('i',[])

n=int(input('enter size of array'))

for i in range(n):
    x=int(input('enter size of array'))
    arr.append(x)

print(arr)

x=int(input("Enter number to find the index"))

k=0
for e in arr:
   if e==x:
       print(k)
       break
   k+=1
else:
    print("Number is not found in the array")

print("finish")

import numpy as np

np_array=np.array([1,2,3,4])

print(np_array)