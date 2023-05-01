s = "aabb"

def swap():
    d = {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = [i]
        else:
            d[s[i]].append(i) 

    print(d)
    arr = [i for i in s]
    l = 0; r = len(arr) - 1
    swap = 0
    #for mid element which does not have its pair
    mid_idx = len(arr)//2
    idx_to_mid = len(arr)-1
    for i in d.values():
        if len(i) % 2 != 0:
            for j in i:
                if abs(j - mid_idx) < idx_to_mid:
                    idx_to_mid = j


    while l < r:
        if arr[l] == arr[r]:
            l += 1; r -= 1
            continue
        if len(d[arr[l]]) > 0 and len(d[arr[r]]) > 0:
            x = d[arr[l]][-1]; y = d[arr[r]][-1]
            d[arr[l]].remove(x); d[arr[r]].remove(y)
            arr[x], arr[y] = arr[y], arr[x]
            swap += abs(y-x)
        l += 1; r -= 1

    print(arr)
    return swap

print(swap())
#the above code DOES NOT SWAP ADJACENT elements

def swapAdj():
    ls = list(s); res = 0

    while ls:
        i = ls.index(ls[-1])

        if i == len(ls) - 1:
            res += len(ls)//2
        else:
            res += i
            ls.pop(i)
        ls.pop()

    print(res)

swapAdj()

