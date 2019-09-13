def bubble_sort(input_list):
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-1):
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
    return input_list
input_list=[10,5,30,50,7,22,99,4]
print(bubble_sort(input_list))

def selection_sort(input_list):
    for i in range(len(input_list)):
        min_pos = i
        for j in range(i,len(input_list)):
            if input_list[j]<input_list[min_pos]:
                min_pos = j
        temp = input_list[min_pos]
        input_list[min_pos] = input_list[i]
        input_list[i] = temp
    return input_list
input_list = [10,4,14,27,66,88,31,45,64,7,100]
print(selection_sort(input_list))


def insertion_sort(input_list):
    for i in range(len(input_list)):
        hole = i
        value = input_list[i]
        while hole>0 and input_list[hole-1]>value:
            input_list[hole]=input_list[hole-1]
            hole -= 1
        input_list[hole] = value
print("*"*20)
input_list=[10,28,30,4,9,55,72,87,0]
print(input_list)
insertion_sort(input_list)
print(input_list)

def merge(left,right,input_list):
    len_a = len(left)
    len_b = len(right)
    i = j = k = 0
    while i<len_a and j<len_b:
        if left[i] <= right[j]:
            input_list[k] = left[i]
            i = i+1
        else:
            input_list[k] = right[j]
            j = j+1
        k = k + 1
    while i<len_a:
        input_list[k] = left[i]
        k = k+1
        i = i+1
    while j<len_b:
        input_list[k] = right[j]
        k = k+1
        j = j+1
# input_list=[None]*8
# merge([1,4,7,9],[3,8,10,15],input_list)
def merge_sort(input_list):
    n = len(input_list)
    if n < 2:
        return
    mid = n//2
    left = [None]*mid
    right = [None]*(n-mid)
    for i in range(mid):
        left[i]=input_list[i]
    for j in range(mid,n):
        right[j-mid]=input_list[j]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,input_list)

print("*"*20)
input_list=[20,3,7,30,14,17,8,2,9]
merge_sort(input_list)
print(input_list)


def quick_sort(input_list,start,end):
    if start < end:
        pindex = partition(input_list,start,end)
        quick_sort(input_list,start,pindex-1)
        quick_sort(input_list,pindex+1,end)

def partition(input_list,start,end):
    pivot = input_list[end]
    pindex = start
    for i in range(start,end):
        if input_list[i]<=pivot:
            temp = input_list[i]
            input_list[i] = input_list[pindex]
            input_list[pindex] = temp
            pindex += 1
    temp = input_list[pindex]
    input_list[pindex] = pivot
    input_list[end] = temp
    return pindex

print("-"*20)
input_list=[10,90,3,6,77,1,55,3,7,3,1,99]
quick_sort(input_list,0,len(input_list)-1)
print(input_list)

