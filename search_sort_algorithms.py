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
# sel_sort(nums)
#print(nums)


# nums = [1,10,10,5,8,99,4]
# #print(nums)
# def ins_sort(nums):
#     for i in range(1,len(nums)):
#         hole = i
#         value = nums[i]
#         while hole>0 and nums[hole-1] > value:
#             nums[hole] = nums[hole-1]
#             hole -= 1
#         nums[hole] = value
# ins_sort(nums)
# print(nums)

def merge(L,R,A):
    i=j=k = 0
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            k += 1
            i += 1
        else:
            A[k] = R[j]
            k += 1
            j += 1
    while i<len(L):
        A[k] = L[i]
        k += 1
        i += 1
    while j<len(R):
        A[k] = R[j]
        k += 1
        j += 1

def merge_sort(A):
    if len(A) < 2:
        return
    n = len(A)
    mid = n//2
    L = [None]*(mid)
    R = [None]*(n-mid)
    for i in range(mid):
        L[i] = A[i]
    for j in range(mid,n):
        R[j-mid] = A[j]
    merge_sort(L)
    merge_sort(R)
    merge(L,R,A)

A=[1,2,10,3,9,4,7]
merge_sort(A)
print(A)
print(list(range(3)))


def partition(A,start,end):
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if A[i] <= pivot:
            temp = A[pindex]
            A[pindex] = A[i]
            A[i] = temp
            pindex += 1

    temp = A[end]
    A[end] = A[pindex]
    A[pindex] = temp
    return pindex

def quick_sort(A,start,end):
    if start<end:
        pindex = partition(A,start,end)
        quick_sort(A,start,pindex-1)
        quick_sort(A,pindex+1,end)

A=[10,3,5,1,2,9,7,33,0]
quick_sort(A,0,len(A)-1)
print(A)