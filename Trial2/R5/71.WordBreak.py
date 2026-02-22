dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]
d = set()
for i in dictionary:
    d.add(i)

def f(s):
    dp = [False for i in range(len(s)+1)]

    dp[0] = True

    for i in range(len(s)):
        for j in range(i+1):
            if dp[j] and s[j:i+1] in d:
                dp[i+1] = True
                break

    return dp[len(s)]

print(f("sam"))