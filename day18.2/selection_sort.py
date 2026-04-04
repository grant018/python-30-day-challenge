numbers = [8, 4, 10, 3, 1, 100, 23, 2]

def selection_sort(nums: list):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(selection_sort(numbers))