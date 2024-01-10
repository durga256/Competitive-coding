def test(wild,pat):
    if len(pat) == 0 and (len(wild) == 0 or wild[-1] == '*'):
        return True
    
    if (wild and wild[0] == '?') or (wild and pat and wild[0] == pat[0]):
        return test(wild[1:],pat[1:])
    
    if len(wild) > 1 and wild[0] == '*' and wild[1] == '*':
        return test(wild[1:], pat)
    
    if len(wild) > 1 and wild[0] == '*' and len(pat) == 0:
        return False
    
    if wild and wild[0] == '*':
        return test(wild, pat[1:]) or test(wild[1:], pat)
    
    if (wild and pat and wild[0] != pat[0]) or (wild and not pat) or(pat and not wild):
        return False

print(test("g*ks", "geeks"))  # Yes 
print(test("ge?ks*", "geeksforgeeks"))  # Yes 
print(test("g*k", "gee"))  # No because 'k' is not in second 
print(test("*pqrs", "pqrst"))  # No because 't' is not in first 
print(test("abc*bcd", "abcdhghgbcd"))  # Yes 
print(test("abc*c?d", "abcd"))  # No because second must have 2 instances of 'c' 
print(test("*c*d", "abcd"))  # Yes 
print(test("*?c*d", "abcd"))  # Yes 
print(test("geeks**", "geeks"))  # Yes 