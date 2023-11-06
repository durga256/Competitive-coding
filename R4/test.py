dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]
d = set()
for i in dictionary:
    d.add(i)

word = 'ilikesamsung'

def f():
    dp = [False]*(len(d)+1)
    dp[0] = True
    for i in range(len(word)+1):
        for j in range(i):
            if dp[j] and word[j:i] in d:
                dp[i] = True
                break

    return dp[len(word)]

print(f())
