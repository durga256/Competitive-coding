s = "malayalam"
s = "A man, a plan, a canal: Panama"

def f(s: str):
    s = s.lower()
    res = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            res += i
    n = len(res)
    for i in range(n//2):
        if res[i] != res[n-i-1]:
            return False
    
    return True

f(s)
