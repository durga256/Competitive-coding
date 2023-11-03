x = "AGGTAB"
y = "GXTXAYB"
dp = [[-1 for i in range(len(y)+1)] for i in range(len(x)+1)]

def print_scs():
    n = len(x); m = len(y)
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                temp_a = dp[i-1][j]; temp_b = dp[i][j-1]
                if temp_a > temp_b:
                    dp[i][j] = temp_a
                else:
                    dp[i][j] = temp_b

    for i in dp:
        print(i)

    print("SCS is:",n + m - dp[n][m])

    i = n; j = m
    s = ""
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            s = x[i-1] + s
            i -= 1; j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                s = y[j-1] + s
                j -= 1
            else:
                s = x[i-1] + s
                i -= 1

    while i > 0:
        s = x[i-1] + s
        i -= 1

    while j > 0:
        s = y[j-1] + s
        j -= 1

    print(s)

print_scs()
    