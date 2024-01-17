# Given an list of integers "arr", return True if the number of occurrences
# of each value in the list is unique or return False otherwise.

def calculate_occurences(arr: list[int]) -> dict[int: int]:
    """calculate the occurences of each element of a list"""
    dic = {}

    for num in arr:
        if num not in dic:
            occurences = arr.count(num)
            dic[num] = occurences

    return dic

def unique_occurences(arr: list[int]) -> bool:
    """determine if there is only unique number of occurences between the integers of a list"""
    number_occurences = calculate_occurences(arr)

    set_occurences = set()
    for occurences in number_occurences.values():
        set_occurences.add(occurences)

    if len(set_occurences) != len(number_occurences.values()):
        return False
    return True

arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

print(unique_occurences(arr1))
print(unique_occurences(arr2))
print(unique_occurences(arr3))