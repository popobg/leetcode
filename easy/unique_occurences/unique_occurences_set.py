# Given an list of integers "arr", return True if the number of occurrences
# of each value in the list is unique or return False otherwise.

# less efficient regarding time execution

def unique_occurences(arr: list[int]) -> bool:
    """determine if there is only unique number of occurences between the integers of a list"""
    set_occurences = set()
    set_numbers = set()

    for num in arr:
        set_numbers.add(num)
        set_occurences.add(arr.count(num))

    if len(set_occurences) != len(set_numbers):
        return False

    return True

arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

print(unique_occurences(arr1))
print(unique_occurences(arr2))
print(unique_occurences(arr3))