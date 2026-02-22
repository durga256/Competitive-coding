ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

def intersection():
    i = j = k  = 0; result = []
    while i < len(ar1) and j < len(ar2) and k < len(ar3):
        if ar1[i] == ar2[j] == ar3[k]:
            result.append(ar1[i])
        min_ele = min(ar1[i], ar2[j], ar3[k])
        if min_ele == ar1[i]:
            i += 1
        if min_ele == ar2[j]:
            j += 1
        if min_ele == ar3[k]:
            k += 1

    print(result)

intersection()

def commonElements (A, B, C, n1, n2, n3):
        # your code here
        i = j = k  = 0; result = []
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k]:
                if (i+1 < n1 and A[i+1] != A[i]) or (j+1 < n2 and B[j+1] != B[j]) or (k+1 < n3 and C[k+1] != C[k]):
                    result.append(A[i])
                elif i == n1-1 or j == n2-1 or k == n3-1:
                    result.append(A[i])
            min_ele = min(A[i], B[j], C[k])
            if min_ele == A[i]:
                i += 1
            if min_ele == B[j]:
                j += 1
            if min_ele == C[k]:
                k += 1
                
        return result

