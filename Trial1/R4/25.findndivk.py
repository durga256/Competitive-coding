#Given an array of size n and a number k, 
#find all elements that appear more than " n/k " times.

arr = [3, 1, 2, 2, 1, 2, 3, 3]; k = 4

def find_freq():
    d = {}
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]]+= 1
        else:
            d[arr[i]] = 1
    print(d)
    freq = len(arr)//k
    res = []
    for i in d.keys():
        if d[i] > freq:
            res.append(i)
    print(res)
    return 

#find_freq()

def moores():
    temp = []; res = 0; freq = len(arr)//k
    for i in range(len(arr)):
        flag_notpresent = 1
        for j in range(len(temp)):
            if temp[j][0] == arr[i]:
                temp[j][1] += 1
                if temp[j][1] > freq:
                    res += 1
                flag_notpresent = 0
        if flag_notpresent:
            temp.append([arr[i], 1])
        
    print(temp)
    print(res)

moores()
