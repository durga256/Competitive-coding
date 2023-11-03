arr = [90,7,-8,98,-45,54,35]

def kadanes():
    result = 0
    temp_sum = 0
    for i in range(len(arr)):
        temp_sum += arr[i]
        if temp_sum > result:
            result = temp_sum
        
        if temp_sum < 0:
            temp_sum = 0

    print(result)

kadanes()