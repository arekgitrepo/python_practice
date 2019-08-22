import pandas as pd

"""
this is a comment

"""
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df=pd.DataFrame(weather_data)

#help('math')

print(df.shape)

i = 1
while i<=3:
    print("hello ",end=" ")
    j = 1
    while j<=4:
        print("python ",end=" ")
        j+=1
    i+=1
    print()

print("*"*20)

print(5//2)

nums = ['1','2','3','9']
nums.insert(2,'10')
print(nums)

import math

del nums[1:3]

print(math.sqrt(25))

print(nums)

nums_tuple = (1,2,3,4,5)
print(nums_tuple.index(3))


# a = input("Enter first number")
# print(type(a))
# b = input("Enter second number")
#
# c = int(a) + int(b)
# print("Answer is %s" %c)

dir(nums)


