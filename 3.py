def sorts(nums):
    squares = [num ** 2 for num in nums]
    squares.sort()
    return squares

nums = [4, -3, 0, -2, 9]
print("Відсортований масив:", sorts(nums))