s = "abbbde"
s = "abcd"

def power():
    ans = []
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            subStr = s[i:i+j]
            ans.append(subStr)
            for k in range(1,len(subStr)):
                ans.append(subStr[:k]+subStr[k+1:])
            ans.append(s[:i+1]+s[j:])

    print(len(ans))
    return ans

print(power())
