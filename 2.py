def number(num):
        count = 0
        while num> 0:
            count += 1
            num//= 10
        return count

def para(num):
        return number(num) % 2 == 0

def numbers(nums):
    count = 0  
    for num in nums:
        if para(num):
            count += 1

    return count

nums = [234, 4567, 12, 344, 4, 3456]
print("Чисел з парною кількістю цифр: ", numbers(nums))
