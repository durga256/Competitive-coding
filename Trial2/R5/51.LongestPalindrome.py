s = "forgeeksskeegfor"
#s = "ac"
s= "aacabdkacaa"
s="xaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
def f():
    res = ''
    for i in range(len(s)):
        #odd length
        l = r = i
        while l>=0 and r< len(s) and s[l] == s[r]:
            resLen = r-l+1
            if resLen > len(res):
                res = s[l:r+1]
            l -= 1; r += 1

        #even length
        l = i; r = i+1
        while l>= 0 and r < len(s) and s[l] == s[r]:
            resLen = r-l+1
            if resLen > len(res):
                res = s[l:r+1]
            l -= 1; r += 1

    print(res)

f()

dp = []
for i in range(len(s)+1):
    dp.append([-1]*(len(s)+1))

def rec(s, l, r):
    #base cases
    if l < 0 or r >= len(s) or l > r:
        return ['', True]
    
    if dp[l][r] != -1:
        return dp[l][r]
    
    if s[l] == s[r]:
        temp = rec(s,l+1,r-1)
        if l != r and temp[1]:
            dp[l][r] = [s[l]+temp[0]+s[r], True]
            return dp[l][r]
        elif l==r and temp[1]:
            dp[l][r] = [s[l], True]
            return dp[l][r]
    temp1 = rec(s,l+1,r)
    temp2 = rec(s,l,r-1)
    if len(temp1[0]) > len(temp2[0]):
        dp[l][r] = [temp1[0], False]
    else:
        dp[l][r] = [temp2[0], False]
    return dp[l][r]
    
print(rec(s,0,len(s)-1)[0])