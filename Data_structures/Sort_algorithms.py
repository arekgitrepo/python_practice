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
