arr = [5, 4, 3, 2, 1]

def bubble_sort(nums: list):
    outer_loop = 0
    inner_loop = 0
    swaps = 0
    for i in range(len(nums)):
        swapped = False
        outer_loop += 1
        for j in range(len(nums) - 1 - i):
            inner_loop += 1
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                swaps += 1
                swapped = True
        if not swapped:
            break
    print(f"Outer: {outer_loop} Inner: {inner_loop} Swaps: {swaps}")
    return nums

def insertion_sort(nums: list):
    outer_loop = 0
    moves = 0
    for i in range(1, len(nums)):
        outer_loop += 1
        current = nums[i]
        position = i - 1
        while position >= 0 and nums[position] > current:
            nums[position + 1] = nums[position]
            moves += 1
            position -= 1
        nums[position + 1] = current
        moves += 1
    print(f"Outer: {outer_loop} Moves: {moves}")
    return nums

def selection_sort(nums: list):
    outer_loop = 0
    inner_loop = 0
    swaps = 0
    for i in range(len(nums)):
        outer_loop += 1
        min_index = i
        for j in range(i + 1, len(nums)):
            inner_loop += 1
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
        swaps += 1
    print(f"Outer: {outer_loop} Inner: {inner_loop} Swaps: {swaps}")
    return nums

arr.sort()
print(arr)