def mountain(arr):
    n = len(arr)
    
    if n < 3:
        return False

    vershina = max(arr)
    vershina_index = arr.index(vershina)

    if vershina_index == 0 or vershina_index == n - 1:
        return False

    for i in range(vershina_index):
        if arr[i] >= arr[i + 1]:
            return False

    for i in range(vershina_index, n - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True

arr = [0, 1, 2, 3, 2, 1]
result = mountain(arr)
print(result)  