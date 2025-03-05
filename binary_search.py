def binary_search(list, item):
    first = 0
    last = len(list) - 1

    while first < last:
        middle = int((first+last)/2)
        result = list[middle]
        if result == item:
            return middle
        if result > item:
            last = middle - 1
        else:
            first = middle + 1
    return None


list = [1, 2, 3, 4, 5, 6]
print(binary_search(list, 8))
