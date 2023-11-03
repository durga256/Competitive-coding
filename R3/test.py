dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]
word = 'ilikesamsung'
def get_dict(words):
    d = set()
    for i in words:
        d.add(i)

    return d

def f():
    d = get_dict(dictionary)

    dp = [False]*(len(word)+1)
    dp[0] = True

    for i in range(len(word)+1):
        for j in range(i):
            if dp[j] and word[j:i] in d:
                dp[i] = True
                break

    print(dp)
    return dp[len(word)]

print(f())

