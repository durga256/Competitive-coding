l = ["cat", "dog", "tac", "god", "act"]

def hash_string(s):
    hash_val = 0
    for i in s:
        hash_val += ord(i)*(2**((ord(i)-96)%13))

    return hash_val

def f():
    d = {    }
    for i in l:
        temp = hash_string(i)
        if temp in d:
            d[temp].append(i)
        else:
            d[temp] = [i]

    for i in d:
        print(d[i])
    

f()

def f2():
    res = arr.copy()
    for i in range(len(arr)):
        temp = list(arr[i])
        temp.sort()
        res[i] = [''.join(temp), i]

    res.sort()
    print(res)
    ans = [[res[0]]]
    prev = res[0]
    for i in range(1,len(res)):
        if prev[0] != res[i][0]:
            ans.append([])
            prev = res[i]
            ans[-1].append(prev)
        else:
            ans[-1].append(res[i])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            ans[i][j] = arr[ans[i][j][1]]

    print(ans)


f2()

