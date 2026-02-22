A = "EACBD";B = "EABCD"
A = "YUZKxQReJATCsD";B= "seCJQKZRTADUxY"

from collections import Counter
# Can do recursive but exceeds recursion depth
def f(A, B): 
    #code here.
    d_A = Counter(A)
    d_B = Counter(B)
    
    for i in d_B:
        if i not in d_A or d_A[i] != d_B[i]:
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

print(f(A,B))
print(f('EACBD', 'EABCD'))