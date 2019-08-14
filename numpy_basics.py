from numpy import *

arr = array([1, 2, 3])

print(arr)
print(arr.dtype)

# arr=arr+5
arr1 = arr.view()

print(id(arr))
print(id(arr1))

print(arr)
print(arr1)
print("*" * 20)
print(arr)
arr1[0] = 7
print(arr1)

arr = array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]

    ]
)

print(arr.size)

new_Arr = arr.reshape(2, 2, 2)
print("*******")
print(new_Arr)
print(new_Arr[0][1][1])

m = matrix('1 2 3;4 5 6')
print(diagonal(m))

m1 = array([

    [1, 2],
    [3, 4]
])

m2 = array([
    [1, 2],
    [3, 4]
])
print("*" * 20)
m3 = zeros([2, 2], int)

#Matrix Multiplication

# if m1.shape[1] == m2.shape[0]:
#     sum = 0
#     for i in range(m1.shape[0]):
#         for j in range(m2.shape[1]):
#             for k in range(m1.shape[1]):
#                 sum += int(m1[i][k] * m2[k][j])
#             m3[i][j] = sum
#             sum = 0
#     print(m3)
# else:
#     print("cannot multiply")


def print_num(**kwargs):
    #print(name)
    #print(kwargs)
    for k,v in kwargs.items():
        print("key is %s and value is %s"%(k,v))

print_num(name=1,name1='anudeep',age='27')

print("*"*20)

a = 10
def func():
    #global a
    globals()['a'] = 12
    a = 11
    print("inside func -"+str(globals()['a']))

    print("inside func local variable - "+str(a))

func()

print("Outside func--"+str(a))

lst=[]

#globals example

# for i in range(3):
#     lst.append(str(input("enter a name")))
#
# max_len=5
# def max_length(lst):
#     count=0
#     for e in lst:
#         if len(e) > globals()['max_len']:
#             count+=1
#     return count
#
# count = max_length(lst)
#
# print("Number of users with max_len = {} are {}".format(max_len,count))

#fibonacci

# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)
# fib(8)

#factorial

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*i
#     return f
#
# print(fact(5))

#recursion

# import sys
#
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
#
# i = 0
# def greet():
#     global i
#     i+=1
#     print("hello ",i)
#     greet()
#
# greet()

# Factorial using Recursion

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# Anonymous / Lambda functions
# f = lambda a,b : a+b
# print(f(10,2))
# from functools import reduce
# lst=[1,2,3,4,5,6,7,8]
# filt = list(filter(lambda a : a%2==0,lst))
# print(filt)
# doubles = list(map(lambda a:a*2,filt))
# print(doubles)
# sum = reduce(lambda a,b:a+b,doubles)
# print(sum)

#Decorators

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
#@smart_div
def div(a,b):
    return a/b
div=smart_div(div)
print(div(2,4))

print(__name__)