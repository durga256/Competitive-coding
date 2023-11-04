s1 = "abcd"
s2 = "cdab"

def checkIf(s1,s2):
    n = len(s1); m = len(s2)
    if n!= m:
        return False
    
    s1 = s1 + s1
    if s2 in s1:
        return True
    else:
        return False

print(checkIf(s1,s2))