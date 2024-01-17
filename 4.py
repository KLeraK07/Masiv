def zero(arr):
    i = 0

    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop() 
            i += 2 
        else:
            i += 1

arr = [0, 0, 2, 1, 0, 5, 3, 0, 5, 7]
zero(arr)
print(arr)