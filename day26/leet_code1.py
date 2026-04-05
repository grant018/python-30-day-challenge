numbers = [3, 2, 4]
target = 6

def find_two(nums, target):
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return(i, j)
            j += 1

def find_two_fast(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return(seen[need], i)
        seen[num] = i


print(find_two(numbers, target))
print(find_two_fast(numbers, target))