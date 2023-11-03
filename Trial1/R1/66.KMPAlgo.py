haystack = "ABABDABACDABABCABAB"
needle = "ABABCABAB"
def find():
    #construct pi table
    N = len(haystack)
    M = len(needle)
    lps = [0]*M
    leng = 0; i = 1
    while i < M:
        if needle[i] == needle[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1    

    print(lps)
    i = 0; j = 0; res = []
    while (N-i) >= (M-j): #Ensuring needle is smaller than haystack
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == M:
            res.append(i-j)
            j = lps[j-1]
        elif i < N and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    print(res)

find()