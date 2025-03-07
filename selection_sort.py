# descending order
def find_highest(arr):
    highest = arr[0]
    highest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index

def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        highest_index = find_highest(arr)
        new_array.append(arr[highest_index])
        arr.pop(highest_index)
    return new_array


print(selection_sort([6, 3, 6, 9 , 2, 11]))