arr = [2, 1, 9, 3, 10, 4, 20]

def lcs():
    d = {}; result = 0; temp_result = 0
    for i in range(len(arr)):
        d[arr[i]] = []
    
    for i in range(len(arr)):
        if arr[i] - 1 not in d.keys():
            j = arr[i]
            while j in d.keys():
                temp_result += 1
                j += 1
        result = max(result, temp_result)
        temp_result = 0

    print(result)

lcs()


        