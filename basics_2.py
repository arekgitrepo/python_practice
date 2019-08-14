# class bike:
#     wheels = 2
#     def __init__(self,year=1999,make='bmw'):
#         self.year = year
#         self.make = make
#     def info(self):
#         print("Make is {}.year of bike is {}".format(self.make,self.year))
#     @classmethod
#     def get_wheel_info(cls):
#         print("wheels of bike are {}".format(cls.wheels))
#     @staticmethod
#     def details():
#         print("this is a bike template")
# b1 = bike(2019,'harley')
# b1.make='hero'
# b2 = bike()
# b1.info()
# bike.wheels=3
# print(b1.wheels)
# b2.info()
# print(b2.wheels)
# bike.get_wheel_info()
# b1.get_wheel_info()
# bike.details()
#
# class Student():
#     def __init__(self,age,name,make,ram):
#         self.age=age
#         self.name=name
#         self.lap=self.Laptop(make,ram)
#     def func(self):
#         pass
#     def show(self):
#         print("Age is {} and name is {}...".format(self.age,self.name))
#         self.lap.show()
#     class Laptop:
#         def __init__(self,make,ram):
#             self.make=make
#             self.ram=ram
#         def show(self):
#             print("Make of laptop is {} and RAM is {}...".format(self.make,self.ram))
#
# def main():
#     s1 = Student(22, 'sunny', 'hp', '8 GB')
#     s2 = Student.Laptop('Lenovo', '4 GB')
#     s1.show()
#     s2.show()
# if __name__ == '__main__':
#    main()
#
# a = 10
# b = 11
# print(a + b)


# class Kid:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self, other):
#         r1 = self.m1 + other.m1
#         r2 = self.m2 + other.m2
#         k3 = Kid(r1,r2)
#         return k3
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False
#     def sum(self,*args):
#         s = 0
#         for e in args:
#             s += e
#         return s
# k1 = Kid(10,20)
# k2 = Kid(30,40)
# k3 = k1+k2
# print(k3.m1,k3.m2)
# print(k2>k1)
# print(int.__add__(10,15))
# print("sum is {}....".format(k1.sum(2,3,10)))
#
#
# lst = [10,20,30]
# it = iter(lst)
#
# print(it.__next__())
#
# class TopTen:
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#          return  self
#     def __next__(self):
#         if self.num <=10:
#             val = self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
# values = TopTen()
# print(next(values))
# for i in values:
#     print(i)
#
# def generator_example(n):
#     for i in range(1,n):
#         yield i
# values=generator_example(11)
# print("*"*20)
# for i in values:
#     print(i)

# a=5
# b=0
# b = int('a')
# print(a / b)
# try:
#     print(a/b)
# except Exception as e:
#     print("Error occurred ",e)

# from threading import *
# from time import sleep
#
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello")
#             sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi")
#             sleep(1)
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("End")

# f = open('sample','r')
# f1 = open('sample_write','a')
# for line in f:
#     f1.write(line)

# pos = -1
# def lin_search(list, n):
#     for i in range(len(list)):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i += 1
#     return False
# list = [20, 10, 30, 40, 50]
# print(list)
# n = 40
# if lin_search(list, n):
#     print("Found at ", pos + 1)
# else:
#     print("Not found")

# pos = -1
# def bin_search(list, n):
#     l = 0
#     u = len(list) - 1
#
#     while l <= u:
#         mid = (l + u) // 2
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid + 1
#             else:
#                 u = mid - 1
#     return False
#
# list = [10, 20, 30, 40, 50]
# n = 30
#
# if bin_search(list, n):
#     print("Found at ", pos + 1)
# else:
#     print("Not found")

# nums = [1,10,10,5,8,99,4]
# print(nums)
# def b_sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# b_sort(nums)
# print(nums)

# nums = [1,10,10,5,8,99,4]
# #print(nums)
# def sel_sort(nums):
#     for i in range(len(nums)-1):
#         minpos = i
#         for j in range(i,len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#         temp = nums[minpos]
#         nums[minpos] = nums[i]
#         nums[i] = temp
#         print(nums)
#
# sel_sort(nums)
# #print(nums)