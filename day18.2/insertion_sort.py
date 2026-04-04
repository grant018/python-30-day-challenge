numbers = [8, 4, 10, 3]

def insertion_sort(nums: list):
    for i in range(1, len(nums)):
        current = nums[i]
        position = i - 1
        while position >= 0 and nums[position] > current:
            nums[position + 1] = nums[position]
            position -= 1
        nums[position + 1] = current
    return nums

print(insertion_sort(numbers))