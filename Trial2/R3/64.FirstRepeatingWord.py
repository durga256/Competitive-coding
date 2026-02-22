s = "Ravi had been saying that he had been there"
s = 'he had had he'

def f():
    ls = s.split()
    dict = set()
    ans = ''
    for i in range(len(ls)-1,-1,-1):
        if ls[i] in dict:
            ans = ls[i]
        else:
            dict.add(ls[i])
    if ans:
        print(ans)
        return
    print('No repeat')

f()