numbers = [20, 15, 44, 11, 199, 457, 113, 1, 449, 123]

def bubble_sort(nums: list):
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

print(bubble_sort(numbers))