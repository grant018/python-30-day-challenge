arr = [2, 6, 7, 5, 4, 45, 53, 23, 65, 84, 33, 101, 3, 1, 432, 532, 1001, 354, 32]
arr.sort()
print(arr)

def binary_search(numbers, target):
    high = len(numbers) - 1
    low = 0
    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

print(binary_search(arr, 65))