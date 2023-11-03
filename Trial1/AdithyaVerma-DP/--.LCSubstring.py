x = "abcde"
y = "cdabe"

def lcs():
    n = len(x); m = len(y)
    dp = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(n+1):
        dp[i][0] = ""
    for i in range(m+1):
        dp[0][i] = ""

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + x[i-1]
            else:
                dp[i][j] = ""

    for i in dp:
        print(i)

lcs()

