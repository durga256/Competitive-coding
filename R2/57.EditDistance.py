str1 = 'geek'; str2 = 'gesek'
str1 = 'cat';str2 = 'cut'
str1 = 'sunday'; str2 = 'saturday'
str1='GEEXSFRGEEKKS';str2='GEEKSFORGEEKS'
#A->B

def f(s1,s2,n,m):
    if n == 0 or m == 0:
        return n+m
    
    if s1[n-1] == s2[m-1]:
        return f(s1,s2,n-1,m-1)
    else:
        return 1+min(f(s1,s2,n-1,m), #remove
                     f(s1,s2,n,m-1),#insert
                     f(s1,s2,n-1,m-1)) #replace
    
temp = f(str1,str2,len(str1), len(str2))
print(temp)
