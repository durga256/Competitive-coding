arr = "geeksforgeeks"

def count_sort():
    output = [0]*len(arr)

    count_arr = [0]*256

    for i in arr:
        count_arr[ord(i)] += 1

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]

    n = len(count_arr)
    for i in range(n-1,0,-1):
        count_arr[i] = count_arr[i-1]

    for i in range(len(arr)):
        output[count_arr[ord(arr[i])]] = arr[i]
        count_arr[ord(arr[i])] += 1

    s = ""
    for i in output:
        s += i

    print(s)

count_sort()