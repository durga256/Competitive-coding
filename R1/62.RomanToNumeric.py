s='XL'
s='MCMIV'
s='IX'
d = {
    'I': 1,'IV': 4,'V': 5,'IX': 9
  ,'X': 10,'XL': 40,'L': 50,'XC': 90,'C': 100,'CD': 400
 ,'D': 500,'CM': 900 ,'M': 1000
}

def f():
    res = d[s[0]]; prev=s[0]
    for i in range(1,len(s)):
        if d[prev] < d[s[i]]:
            res -= d[prev]*2
        res += d[s[i]]
        prev = s[i]

    print(res)

f()