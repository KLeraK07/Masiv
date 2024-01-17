def one(nums):
    suma = 0 #Максимальної кількості повторень 1-ці
    current_count = 0  # Поточної кількості повторень 1-ці

    for num in nums:
        if num == 1:
            current_count += 1
            suma = max(suma, current_count)
        else:
            current_count = 0

    return suma

# Приклад використання:
nums = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]
print("Максимальна кількість повторень 1-ці:", one(nums))

