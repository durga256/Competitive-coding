arr = [ ["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]
R = len(arr)
C = len(arr[0])


res = []
def f(L, row_idx, ip):
    if row_idx == len(L):
        res.append(ip)
        return 
    
    for i in range(len(L[row_idx])):
        if L[row_idx][i]:
            f(L, row_idx+1, ip+[L[row_idx][i]])

f(L, 0, [])

def f(arr,m,n,output):
    output[m] = arr[m][n]

    if m+1 < R:
        for i in range(C):
            if arr[m+1][i] != "":
                f(arr,m+1,i,output)
    
    if m == R-1:
        print(' '.join(output))
        return
    
def f2():
    # Create an array to store sentence - max length of any sentence = R words
    output = [""] * R
    for i in range(C):
        if arr[0][i] != "":
            f(arr,0,i,output)

f2()