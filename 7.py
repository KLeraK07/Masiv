def double(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False

arr = [7, 2, 4, 4, 10, 3]
result = double(arr)
print(result) 