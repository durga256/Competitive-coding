def f(s1,s2):
    #if both string empty return true
    if len(s1)== 0 and len(s2)== 0:
        return True
    
    #remove consecutive stars in beginning
    if len(s1) > 1 and s1[0] == '*':
        i = 0
        while i+1 < len(s1) and s1[i+1] == '*':
            i = i+1
        s1 = s1[i:]

    #check if chars after * in first are present in second
    if len(s1) > 1 and s1[0] == '*' and len(s2) == 0:
        return False
    
    #if ? or char match move on to next
    if (len(s1)!= 0 and s1[0] == '?') or (len(s1)!=0 and len(s2)!=0 and s1[0]==s2[0]):
        return f(s1[1:], s2[1:])
    
    #if * we either include the char in s2 in out * or not
    if len(s1) != 0 and s1[0] == '*':
        return f(s1[1:], s2) or f(s1,s2[1:])



f("abc*bcd", "abcdhghgbcd")
    