A = "EACBD";B = "EABCD"
A = "YUZKxQReJATCsD";B= "seCJQKZRTADUxY"
    
def f2(A,B):
    dB = {}
    if len(A) != len(B):
        return -1
    
    for i in range(len(B)):
        if B[i] in dB:
            dB[B[i]] += 1
        else:
            dB[B[i]] = 1

    for i in range(len(A)):
        if A[i] not in dB:
            return -1
        else:
            dB[A[i]] -= 1

    for i in dB:
        if dB[i] != 0:
            return -1
        
    n = len(A)
    i = n-1; j = n-1; res = 0
    while i >= 0:
        while i >= 0 and A[i] != B[j]:
            i -= 1
            res += 1

        if i >= 0:
            i -= 1
            j -= 1

    return res

print(f2(A,B))




f2(A,B)