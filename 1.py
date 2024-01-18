def one(nums):
    suma = 0 
    current_count = 0 

    for num in nums:
        if num == 1:
            current_count += 1
            suma = max(suma, current_count)
        else:
            current_count = 0

    return suma

nums = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]
print("Максимальна кількість повторень 1-ці:", one(nums))

