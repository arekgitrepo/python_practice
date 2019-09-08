def lin_search(input_list,item):
    for i in range(len(input_list)):
        if item == input_list[i]:
            return i
    return None
l1 = [2,7,1,4,10,6]
item = 7
print(lin_search(l1,item))

def lin_search_ordered(input_list,item):
    for i in range(len(input_list)):
        if input_list[i] == item:
            return i
        elif input_list[i] > item:
            return None
    return None
l1 = [1,2,3,5,6]
item = 4
print(lin_search_ordered(l1,item))


def bin_search(input_list,item):
    start_index = 0
    end_index = len(input_list)-1
    while start_index <= end_index:
        mid_index = (start_index+end_index)//2
        if input_list[mid_index] == item:
            return mid_index
        if item > input_list[mid_index]:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return None
input_list = [10,20,25,45,50,70,90,100]
item = 100
print(bin_search(input_list,item))

def bin_search_recursive(input_list,start_index,end_index,item):
    if start_index>end_index:
        return None
    else:
        mid_index = (start_index+end_index)//2
        if input_list[mid_index] == item:
            return mid_index
        elif item > input_list[mid_index]:
            return bin_search_recursive(input_list,mid_index+1,end_index,item)
        else:
            return bin_search_recursive(input_list,start_index,mid_index-1,item)

input = [10,30,50,60,70,90,120]
item = 120
print(bin_search_recursive(input,0,len(input)-1,item))