s = 'aabcbcdbca'
def f():
    distinct = len(set(str))
    dic = {}
    ans = len(str)
    i,j = 0,0
    while i<len(str):
        if str[i] in dic:
            dic[str[i]] += 1
        else:
            dic[str[i]] = 1
        if distinct == len(dic):
            while dic[str[j]] > 1:
                dic[str[j]] -= 1
                j += 1
            ans = min(ans,i-j+1)
        i += 1

    return ans

f()