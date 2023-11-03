s = "cbbd"

def longest():
    res = ""
    resLen = 0
    for i in range(len(s)):
        #odd length
        l = r = i
        while s[l] == s[r] and l >= 0 and r < len(s):
            if r-l + 1 > resLen:
                resLen = r-l+1
                res = s[l:r+1]
            l -= 1; r += 1
        
        #even length
        l = i; r = i + 1
        while s[l] == s[r] and l >=0 and r < len(s):
            if r-l + 1 > resLen:
                resLen = r-l+1
                res = s[l:r+1]
            l -= 1; r += 1
    
    return res



            