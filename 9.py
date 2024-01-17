def max_element(arr):
    n = len(arr)
    
    if n == 1:
        return [-1]
        
    right_max = -1  

    for i in range(n - 1, -1, -1):
        emp = arr[i] 
        arr[i] = right_max
        right_max = max(right_max, emp)

    return arr

arr = [3, 0, 13, -5, 7, -3, 1]
result = max_element(arr)
print("Отриманий масив:", result) 