def sub_none_to_medium(arr):
    index_of_none = arr.index(None)
    arr[index_of_none] = sum(arr[:index_of_none] + arr[index_of_none + 1:]) / len(arr)

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print(f'Исходный список: {numbers}')
sub_none_to_medium(numbers)
print(f'None -> mean список: {numbers}')