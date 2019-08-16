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


