def sorting(nums):
    parni = [num for num in nums if num % 2 == 0]
    neparni = [num for num in nums if num % 2 != 0]
    return parni + neparni

nums = [0, 4, -1, 3, 2,  7, -6]
result = sorting(nums)
print("Отриманий масив:", result) 