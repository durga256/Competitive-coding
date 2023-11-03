haystack = 'ababcabcabababd'
needle = 'ababd'
# needle = 'abcdabeabf'
# needle = 'abcdeabfabc'
# needle = 'aabcadaabe'

def kmp():
    #construct pi table
    N = len(haystack)
    M = len(needle)
    lps = [0]*(M)
    prefix_idx = 0; i = 1
    while i < M:
        if needle[i] == needle[prefix_idx]:
            prefix_idx += 1
            lps[i] = prefix_idx
            i += 1
        else:
            if prefix_idx != 0:
                prefix_idx = lps[prefix_idx-1]
            else:
                lps[i] = 0
                i += 1    

    print(lps)

    i = 0; j = 0; res=[]
    while (N-i) >= (M-j):
        if needle[j] == haystack[i]:
            i += 1
            j += 1
        if j == M:
            res.append(i-j)
            j = lps[j-1]
        elif i < N and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    print(res)

kmp()