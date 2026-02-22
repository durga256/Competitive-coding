arr = [170, 45, 75, 90, 802, 24, 2, 66]
def count_sort(arr, exp):
    output = [0]*len(arr)
    count_arr = [0]*10

    for i in range(len(arr)):
        index = arr[i] //exp
        count_arr[index%10] += 1

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(count_arr)-1,0,-1):
        count_arr[i] = count_arr[i-1]

    count_arr[0] = 0

    for i in range(len(arr)):
        index = arr[i] //exp
        output[count_arr[index%10]] = arr[i]
        count_arr[index%10] += 1

    for i in range(len(output)):
        arr[i] = output[i]

    print(arr)
    return arr

def radix_sort(arr):
    max1 = max(arr)
    exp = 1

    while max1//exp >= 1:
        arr = count_sort(arr, exp)
        exp *= 10

radix_sort(arr)

    




