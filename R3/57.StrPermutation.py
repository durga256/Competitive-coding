s = "ABC"
ans = ""

def permute(s, ans):
    if len(s) == 0:
        print(ans, end=" ")
        return
    
    for i in range(len(s)):
        ch = s[i]
        left_str = s[0:i]
        right_str = s[i+1:]
        not_used = left_str + right_str
        permute(not_used, ans+ch)
    
permute(s,ans)