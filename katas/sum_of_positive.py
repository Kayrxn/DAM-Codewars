def positive_sum(arr):
    total = 0                
    for n in arr:
        if n > 0:
            total = total + n
    return total