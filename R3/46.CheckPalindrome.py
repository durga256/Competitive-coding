s = "malayialam"

def f():
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
        
    return True

print(f())